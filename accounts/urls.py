from django.urls import path
from .views import register, login, user_profile

urlpatterns = [
    path('create/', register, name='register'),
    path('login/', login, name='login'),
    path('accounts/<str:username>/', user_profile, name='user-profile'),
]