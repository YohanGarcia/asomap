from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet

# Router estándar (lowercase, con slash final)
router = DefaultRouter()
router.register(r'about', AboutViewSet, basename='about')

# Router adicional para endpoints EXACTOS solicitados (mayúsculas y sin slash final)
class NoSlashRouter(DefaultRouter):
    trailing_slash = ''

router_caps = NoSlashRouter()
router_caps.register(r'About', AboutViewSet, basename='About-exact')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += router_caps.urls