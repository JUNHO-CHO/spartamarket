from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'image', 'author']  # 이미지 필드 포함
        read_only_fields = ['author']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        if validated_data.get('image'):
            instance.image = validated_data.get('image')  # 이미지 수정 처리
        instance.save()
        return instance

