from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Footer
from .serializers import FooterSerializer

@extend_schema_view(
    list=extend_schema(
        summary="Listar footers",
        description="Retorna una lista de elementos de footer activos",
        tags=['layout']
    ),
    retrieve=extend_schema(
        summary="Obtener footer",
        description="Retorna un elemento específico de footer por ID",
        tags=['layout']
    ),
    create=extend_schema(
        summary="Crear footer",
        description="Crea un nuevo elemento de footer",
        tags=['layout']
    ),
    update=extend_schema(
        summary="Actualizar footer",
        description="Actualiza completamente un elemento de footer",
        tags=['layout']
    ),
    partial_update=extend_schema(
        summary="Actualización parcial de footer",
        description="Actualiza parcialmente un elemento de footer",
        tags=['layout']
    ),
    destroy=extend_schema(
        summary="Eliminar footer",
        description="Elimina un elemento de footer",
        tags=['layout']
    )
)
class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    
    def get_queryset(self):
        """
        Retorna el queryset apropiado según la acción
        """
        return Footer.objects.filter(is_active=True)
    
    def list(self, request, *args, **kwargs):
        """
        Listar footers
        
        Retorna una lista de elementos de footer activos
        """
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener footer
        
        Retorna un elemento específico de footer por ID
        """
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        """
        Crear footer
        
        Crea un nuevo elemento de footer
        """
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
        Actualizar footer
        
        Actualiza completamente un elemento de footer
        """
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Actualización parcial de footer
        
        Actualiza parcialmente un elemento de footer
        """
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar footer
        
        Elimina un elemento de footer
        """
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        summary="Obtener información del footer",
        description="Retorna la información del footer del sitio web de ASOMAP",
        responses={200: FooterSerializer, 404: None},
        tags=['layout']
    )
    @action(detail=False, methods=['get'], url_path='footer')
    def footer(self, request):
        """
        Obtener información del footer
        
        Retorna la información del footer del sitio web de ASOMAP
        """
        try:
            footer = get_object_or_404(Footer.objects.filter(is_active=True))
            serializer = FooterSerializer(footer)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': 'Footer not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
