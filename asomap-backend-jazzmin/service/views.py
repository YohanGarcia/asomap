from rest_framework import viewsets
from .models import ServicesPage, ServiceInfo
from .serializers import ServicesPageSerializer, ServiceInfoSerializer


class ServicesPageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para manejar la página de servicios bancarios
    Solo permite lectura (GET)
    """
    queryset = ServicesPage.objects.filter(is_active=True)
    serializer_class = ServicesPageSerializer
    
    def get_queryset(self):
        """Retorna solo la página activa con sus servicios"""
        return super().get_queryset().prefetch_related(
            'item_details'
        ).filter(
            is_active=True,
            item_details__is_active=True
        ).distinct()


class ServiceInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para manejar información detallada de servicios
    Solo permite lectura (GET)
    """
    queryset = ServiceInfo.objects.filter(is_active=True)
    serializer_class = ServiceInfoSerializer
    
    def get_queryset(self):
        """Retorna solo servicios activos"""
        return super().get_queryset().filter(is_active=True)
