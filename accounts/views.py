from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import CustomUserSerializer

User = get_user_model()

# 회원가입 뷰
class RegisterView(APIView):

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 로그인 뷰
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 사용자 인증
        user = authenticate(username=username, password=password)

        if user is not None:
            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)  # access_token을 문자열로 변환 후 반환

            return Response({
                'refresh': str(refresh),
                'access': access_token,  # access_token을 반환
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'detail': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)

# 프로필 조회 뷰
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        # 프로필 조회 대상 사용자 찾기
        user = get_object_or_404(User, username=username)

        # 반환할 사용자 정보
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
        }

        return Response(user_data, status=status.HTTP_200_OK)

