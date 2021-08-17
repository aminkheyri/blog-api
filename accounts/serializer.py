from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'phone', 'email', 'first_name', 'last_name', 'last_login', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }


class PhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField()


class RandomCodeSerializer(serializers.Serializer):
    phone = serializers.CharField()
    random_code = serializers.IntegerField()
