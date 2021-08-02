from rest_framework import routers
from posts.views import PostViewSet


router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')