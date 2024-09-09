from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.exceptions import PermissionDenied
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import DestroyAPIView

# Create your views here.
class ProductCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPagination(PageNumberPagination):
    page_size = 10  # 페이지당 항목 수 설정

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = []

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        product = self.get_object()
        if self.request.user != product.author:
            raise PermissionDenied("수정 권한이 없습니다.")
        serializer.save()


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.author:  # 작성자만 삭제 가능
            raise PermissionDenied("삭제 권한이 없습니다.")
        instance.delete()






        class ProductDetailAPIView(APIView):
            permission_classes = [IsAuthenticated]

            def get_object(self, pk):
                return get_object_or_404(Product, pk=pk)

            def get(self, request, pk):  # 상품 세부 목록 조회
                product = self.get_object(pk)
                serializer = ProductSerializer(product)
                return Response(serializer.data)

            def put(self, request, pk):  # 상품 수정
                product = self.get_object(pk)
                if request.user != product.author:
                    raise PermissionDenied("수정이 불가능 합니다.")
                serializer = ProductSerializer(product, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)

            def delete(self, request, pk):  # 상품 삭제
                product = self.get_object(pk)
                if request.user != product.author:
                    raise PermissionDenied("삭제가 불가능 합니다.")
                product.delete()
                return Response({"message": f"상품 ({pk})를 삭제했습니다."}, status=status.HTTP_204_NO_CONTENT)

            def delete(self, request, pk):  # 상품 삭제
                products = self.get_object(pk)  # 지울 products 조회
                if request.user != products.author:
                    raise PermissionDenied("삭제안됨")
                products.delete()
                data = {"delete": f"Product({pk}) is deleted."}
                return Response(data, status=status.HTTP_200_OK)