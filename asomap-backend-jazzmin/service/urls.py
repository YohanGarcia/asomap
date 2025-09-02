from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicesPageViewSet, ServiceInfoViewSet

router = DefaultRouter()
router.register(r'services', ServicesPageViewSet, basename='services')
router.register(r'service-info', ServiceInfoViewSet, basename='service-info')

urlpatterns = [
    path('', include(router.urls)),
]
