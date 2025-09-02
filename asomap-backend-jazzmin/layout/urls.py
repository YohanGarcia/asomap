from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LayoutViewSet

# Router estándar (lowercase)
router = DefaultRouter()
router.register(r'layout', LayoutViewSet, basename='layout')

# Router adicional para endpoint EXACTO (mayúsculas, sin slash final)
class NoSlashRouter(DefaultRouter):
    trailing_slash = ''

router_caps = NoSlashRouter()
router_caps.register(r'layout', LayoutViewSet, basename='layout-exact')  # 'layout' ya es minúscula

urlpatterns = []
urlpatterns += router.urls
urlpatterns += router_caps.urls