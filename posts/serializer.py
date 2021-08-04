from rest_framework import serializers
from .models import Article, Comment, Likes
from accounts.serializer import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'body', 'created_at',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'reply', 'is_reply', 'body', 'created',)


class LikesSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # total_likes = serializers.SerializerMethodField()
    # likes_by = UserSerializer(many=True)
    #
    # def total_likes(self, instance):
    #     return instance.likes_by.count()

    class Meta:
        model = Likes
        fields = ('id', 'user', 'post')