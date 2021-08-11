from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import permissions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'phone', 'email', 'first_name', 'last_name', 'last_login', 'is_superuser')
