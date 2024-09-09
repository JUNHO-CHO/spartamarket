from django.urls import path
from .views import  ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView


urlpatterns=[
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]