from django.urls import path
from .views import RegisterView, LoginView, UserProfileView

# 회원가입 엔드포인트 설정
urlpatterns = [
    path('create/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
path('accounts/<str:username>/', UserProfileView.as_view(), name='user-profile'),
]