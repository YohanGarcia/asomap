from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Navigation, ExchangeRate
from .serializers import NavigationSerializer, ExchangeRateSerializer, HeaderCompleteSerializer

@extend_schema_view(
    list=extend_schema(
        summary="Listar navegación",
        description="Retorna una lista de elementos de navegación activos",
        tags=['header']
    ),
    retrieve=extend_schema(
        summary="Obtener elemento de navegación",
        description="Retorna un elemento específico de navegación por ID",
        tags=['header']
    ),
    create=extend_schema(
        summary="Crear elemento de navegación",
        description="Crea un nuevo elemento de navegación",
        tags=['header']
    ),
    update=extend_schema(
        summary="Actualizar elemento de navegación",
        description="Actualiza completamente un elemento de navegación",
        tags=['header']
    ),
    partial_update=extend_schema(
        summary="Actualización parcial de navegación",
        description="Actualiza parcialmente un elemento de navegación",
        tags=['header']
    ),
    destroy=extend_schema(
        summary="Eliminar elemento de navegación",
        description="Elimina un elemento de navegación",
        tags=['header']
    )
)
class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Navigation.objects.all()
    serializer_class = NavigationSerializer
    
    def get_queryset(self):
        """
        Retorna el queryset apropiado según la acción
        """
        return Navigation.objects.filter(is_active=True)
    
    def list(self, request, *args, **kwargs):
        """
        Listar navegación
        
        Retorna una lista de elementos de navegación activos
        """
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener elemento de navegación
        
        Retorna un elemento específico de navegación por ID
        """
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        """
        Crear elemento de navegación
        
        Crea un nuevo elemento de navegación
        """
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
        Actualizar elemento de navegación
        
        Actualiza completamente un elemento de navegación
        """
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Actualización parcial de navegación
        
        Actualiza parcialmente un elemento de navegación
        """
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar elemento de navegación
        
        Elimina un elemento de navegación
        """
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        summary="Obtener datos de navegación",
        description="Retorna la estructura de navegación del sitio web de ASOMAP",
        responses={200: NavigationSerializer(many=True), 404: None},
        tags=['header']
    )
    @action(detail=False, methods=['get'], url_path='navigation')
    def navigation(self, request):
        """
        Obtener datos de navegación
        
        Retorna la estructura de navegación del sitio web de ASOMAP
        """
        try:
            navigation_items = Navigation.objects.filter(is_active=True)
            serializer = NavigationSerializer(navigation_items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': 'Navigation not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'], url_path='exchange')
    def exchange(self, request):
        """
        Obtener tasas de cambio
        
        Retorna las tasas de cambio actuales de ASOMAP
        """
        try:
            exchange_rate = ExchangeRate.objects.filter(is_active=True).first()
            if exchange_rate:
                serializer = ExchangeRateSerializer(exchange_rate)
                return Response(serializer.data)
            return Response(
                {'error': 'Exchange rates not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': 'Exchange rates not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(
        summary="Obtener datos completos del header",
        description="Retorna la estructura completa del header con navegación y tasas de cambio",
        responses={200: HeaderCompleteSerializer, 404: None},
        tags=['header']
    )
    @action(detail=False, methods=['get'], url_path='header-data')
    def header_data(self, request):
        """
        Obtener datos completos del header
        
        Retorna la estructura completa del header que coincide con la estructura del frontend
        """
        try:
            # Obtener navegación
            navigation_items = Navigation.objects.filter(is_active=True)
            navigation_data = {}
            for item in navigation_items:
                navigation_data[item.navigation_type] = item.get_navigation_type_display()
            
            # Obtener tasas de cambio
            exchange_rate = ExchangeRate.objects.filter(is_active=True).first()
            exchange_data = {
                'base': 'Tasa de Cambio',
                'lastUpdated': exchange_rate.last_updated_iso if exchange_rate else None,
                'showBuyRate': exchange_rate.show_buy_rate if exchange_rate else True,
                'showSellRate': exchange_rate.show_sell_rate if exchange_rate else False,
                'rates': exchange_rate.rates_for_frontend if exchange_rate else []
            }
            
            response_data = {
                'navigation': navigation_data,
                'exchange': exchange_data
            }
            
            return Response(response_data)
            
        except Exception as e:
            return Response(
                {
                    'error': 'Header data not found',
                    'debug_info': {
                        'exception': str(e),
                        'navigation_count': Navigation.objects.filter(is_active=True).count(),
                        'exchange_rate_exists': ExchangeRate.objects.filter(is_active=True).exists()
                    }
                }, 
                status=status.HTTP_404_NOT_FOUND
            ) 