from django.contrib import admin
from .models import Post, Comment, Vote


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', '__str__', 'post', 'is_reply')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Vote)


