from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeaderViewSet

# Router estándar (lowercase)
router = DefaultRouter()
router.register(r'header', HeaderViewSet, basename='header')

# Router adicional para endpoints EXACTOS (mayúsculas, sin slash final)
class NoSlashRouter(DefaultRouter):
    trailing_slash = ''

router_caps = NoSlashRouter()
router_caps.register(r'Header', HeaderViewSet, basename='Header-exact')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += router_caps.urls