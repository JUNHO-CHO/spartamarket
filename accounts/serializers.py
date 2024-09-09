from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # 비밀번호 필드는 쓰기 전용으로 설정 (클라이언트가 읽을 수 없도록)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    class Meta:
        model = CustomUser  # CustomUser 모델 연결
        fields = ['username', 'password', 'email', 'first_name',
                  'last_name', 'nickname', 'birthday', 'gender', 'bio']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            nickname=validated_data['nickname'],
            birthday=validated_data['birthday'],
            gender=validated_data.get('gender', ''),
            bio=validated_data.get('bio', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user