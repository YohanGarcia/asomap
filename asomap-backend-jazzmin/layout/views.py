from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Footer, SocialNetwork, Contact
from .serializers import FooterSerializer, SocialNetworkSerializer, ContactSerializer

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

@extend_schema_view(
    list=extend_schema(
        summary="Listar redes sociales",
        description="Retorna una lista de redes sociales activas",
        tags=['layout']
    ),
    retrieve=extend_schema(
        summary="Obtener red social",
        description="Retorna una red social específica por ID",
        tags=['layout']
    ),
    create=extend_schema(
        summary="Crear red social",
        description="Crea una nueva red social",
        tags=['layout']
    ),
    update=extend_schema(
        summary="Actualizar red social",
        description="Actualiza completamente una red social",
        tags=['layout']
    ),
    partial_update=extend_schema(
        summary="Actualización parcial de red social",
        description="Actualiza parcialmente una red social",
        tags=['layout']
    ),
    destroy=extend_schema(
        summary="Eliminar red social",
        description="Elimina una red social",
        tags=['layout']
    )
)
class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer
    
    def get_queryset(self):
        """
        Retorna el queryset apropiado según la acción
        """
        return SocialNetwork.objects.filter(is_active=True).order_by('order', 'name')
    
    def list(self, request, *args, **kwargs):
        """
        Listar redes sociales
        
        Retorna una lista de redes sociales activas ordenadas por orden y nombre
        """
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener red social
        
        Retorna una red social específica por ID
        """
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        """
        Crear red social
        
        Crea una nueva red social
        """
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
        Actualizar red social
        
        Actualiza completamente una red social
        """
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Actualización parcial de red social
        
        Actualiza parcialmente una red social
        """
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar red social
        
        Elimina una red social
        """
        return super().destroy(request, *args, **kwargs)

@extend_schema_view(
    list=extend_schema(
        summary="Listar contactos",
        description="Retorna una lista de contactos activos",
        tags=['layout']
    ),
    retrieve=extend_schema(
        summary="Obtener contacto",
        description="Retorna un contacto específico por ID",
        tags=['layout']
    ),
    create=extend_schema(
        summary="Crear contacto",
        description="Crea un nuevo contacto",
        tags=['layout']
    ),
    update=extend_schema(
        summary="Actualizar contacto",
        description="Actualiza completamente un contacto",
        tags=['layout']
    ),
    partial_update=extend_schema(
        summary="Actualización parcial de contacto",
        description="Actualiza parcialmente un contacto",
        tags=['layout']
    ),
    destroy=extend_schema(
        summary="Eliminar contacto",
        description="Elimina un contacto",
        tags=['layout']
    )
)
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        """
        Retorna el queryset apropiado según la acción
        """
        return Contact.objects.filter(is_active=True).order_by('order', 'name')
    
    def list(self, request, *args, **kwargs):
        """
        Listar contactos
        
        Retorna una lista de contactos activos ordenados por orden y nombre
        """
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener contacto
        
        Retorna un contacto específico por ID
        """
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        """
        Crear contacto
        
        Crea un nuevo contacto
        """
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
        Actualizar contacto
        
        Actualiza completamente un contacto
        """
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Actualización parcial de contacto
        
        Actualiza parcialmente un contacto
        """
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar contacto
        
        Elimina un contacto
        """
        return super().destroy(request, *args, **kwargs)
