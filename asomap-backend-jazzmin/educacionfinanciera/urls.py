from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavingTipViewSet, SliderSlideViewSet, FAQItemViewSet

# Crear el router para los ViewSets
router = DefaultRouter()
router.register(r'saving-tips', SavingTipViewSet, basename='saving-tips')
router.register(r'slider-slides', SliderSlideViewSet, basename='slider-slides')
router.register(r'faq', FAQItemViewSet, basename='faq')

urlpatterns = [
    path('', include(router.urls)),
]
