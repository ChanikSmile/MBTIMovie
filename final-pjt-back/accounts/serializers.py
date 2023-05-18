from django.db import models
from .models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'mbtis', 'genders')
        extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드 설정

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)  # 비밀번호 설정
        user.save()
        return user