from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

# Router estándar (lowercase)
router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

# Router adicional para endpoints EXACTOS (mayúsculas, sin slash final)
class NoSlashRouter(DefaultRouter):
    trailing_slash = ''

router_caps = NoSlashRouter()
router_caps.register(r'news', NewsViewSet, basename='news-exact')  # mismo path, sin slash

urlpatterns = []
urlpatterns += router.urls
urlpatterns += router_caps.urls
