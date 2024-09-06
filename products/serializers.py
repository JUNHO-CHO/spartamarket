from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # 직렬화 할 모델
        fields = ['title','content','image'] #반환값
        # read_only_fields = ('created_at')  #읽기만 할것들

