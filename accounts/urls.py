from django.urls import path
from .views import RegisterView, LoginView

# 회원가입 엔드포인트 설정
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]