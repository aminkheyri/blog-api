from django.contrib import admin
from .models import Article, Comment, Likes


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', '__str__', 'post', 'is_reply')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Likes)


