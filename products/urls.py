from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView
from django.conf import settings  # settings 모듈 추가
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

if settings.DEBUG:  # settings.DEBUG 확인 후 미디어 파일 처리
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)