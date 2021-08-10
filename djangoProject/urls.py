from django.contrib import admin
from django.urls import path, include
from .router_urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('posts.urls', namespace='posts')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
