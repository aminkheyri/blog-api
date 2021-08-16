from rest_framework import routers
from posts.api_views import ArticleViewSet, LikeViewSet, CommentViewSet, ReplyViewSet
from accounts.api_views import UserViewSet


router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('accounts', UserViewSet, basename='accounts')
router.register('comments', CommentViewSet, basename='comments')
router.register('likes', LikeViewSet, basename='likes')
router.register('reply', ReplyViewSet, basename='reply')
