from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
from djangoProject.permissions import IsSuperUser


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]
