from rest_framework import routers
from posts.views import PostViewSet
from accounts.views import UserViewSet


router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('accounts', UserViewSet, basename='accounts')