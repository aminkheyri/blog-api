from rest_framework import serializers
from django.contrib.auth import get_user_model


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'phone', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'phone', 'email', 'first_name', 'last_name', 'last_login', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }
