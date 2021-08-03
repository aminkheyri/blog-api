from rest_framework import routers
from posts.api_views import PostViewSet, VoteViewSet, CommentViewSet
from accounts.api_views import UserViewSet


router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('accounts', UserViewSet, basename='accounts')
router.register('comments', CommentViewSet, basename='comments')
router.register('votes', VoteViewSet, basename='votes')