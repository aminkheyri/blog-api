from rest_framework import viewsets
from .models import Article, Comment, Likes
from .serializer import ArticleSerializer, CommentSerializer, LikesSerializer
from djangoProject.permissions import IsStaffOrReadOnly, IsAuthorOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    ordering_fields = ['author', 'created_at', 'title']
    search_fields = [
        'title',
        'body',
        'author__username',
    ]

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    ordering_fields = ['user', 'post', 'created']
    search_fields = ['post']

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    ordering_fields = ['user', 'post']
    search_fields = ['user', 'post']

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class ShowComment(APIView):
    def post(self, request, pk):
        queryset = get_object_or_404(Article, pk=pk)
