from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LayoutViewSet, SocialNetworkViewSet, ContactViewSet

# Router estándar (lowercase)
router = DefaultRouter()
router.register(r'layout', LayoutViewSet, basename='layout')
router.register(r'social-networks', SocialNetworkViewSet, basename='social-networks')
router.register(r'contacts', ContactViewSet, basename='contacts')

# Router adicional para endpoint EXACTO (mayúsculas, sin slash final)
class NoSlashRouter(DefaultRouter):
    trailing_slash = ''

router_caps = NoSlashRouter()
router_caps.register(r'layout', LayoutViewSet, basename='layout-exact')  # 'layout' ya es minúscula
router_caps.register(r'social-networks', SocialNetworkViewSet, basename='social-networks-exact')
router_caps.register(r'contacts', ContactViewSet, basename='contacts-exact')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += router_caps.urls