from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True)  # 이미지 추가
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






