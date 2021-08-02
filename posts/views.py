from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import responses


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
