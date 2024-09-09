from django.db import models
from django.conf import settings

class Product(models.Model):
    objects = None
    title = models.CharField(max_length=100)  # 상품 제목
    content = models.TextField(blank=True)  # 상품 상세 설명 (빈 값 허용)
    image = models.ImageField(upload_to='products/', blank=True)  # 상품 이미지 (빈 값 허용)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시각 (자동 기록)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title



