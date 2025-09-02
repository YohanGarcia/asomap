from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import News, Promotion
from .serializers import NewsSerializer, PromotionSerializer

class NewsPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

@extend_schema_view(
    list=extend_schema(
        summary="Listar noticias",
        description="Retorna una lista paginada de noticias activas",
        tags=['news']
    ),
    retrieve=extend_schema(
        summary="Obtener noticia",
        description="Retorna una noticia específica por ID",
        tags=['news']
    ),
    create=extend_schema(
        summary="Crear noticia",
        description="Crea una nueva noticia",
        tags=['news']
    ),
    update=extend_schema(
        summary="Actualizar noticia",
        description="Actualiza completamente una noticia",
        tags=['news']
    ),
    partial_update=extend_schema(
        summary="Actualización parcial de noticia",
        description="Actualiza parcialmente una noticia",
        tags=['news']
    ),
    destroy=extend_schema(
        summary="Eliminar noticia",
        description="Elimina una noticia",
        tags=['news']
    )
)
class NewsViewSet(viewsets.ModelViewSet):
    pagination_class = NewsPagination
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        """
        Retorna el queryset apropiado según la acción
        """
        return News.objects.filter(is_active=True)
    
    def list(self, request, *args, **kwargs):
        """
        Listar noticias
        
        Retorna una lista paginada de noticias activas
        """
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Obtener noticia
        
        Retorna una noticia específica por ID
        """
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        """
        Crear noticia
        
        Crea una nueva noticia
        """
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        """
        Actualizar noticia
        
        Actualiza completamente una noticia
        """
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Actualización parcial de noticia
        
        Actualiza parcialmente una noticia
        """
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Eliminar noticia
        
        Elimina una noticia
        """
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        summary="Obtener últimas noticias",
        description="Retorna las noticias más recientes de ASOMAP",
        responses={200: NewsSerializer(many=True), 404: None},
        tags=['news']
    )
    @action(detail=False, methods=['get'], url_path='latest')
    def latest(self, request):
        """
        Obtener últimas noticias
        
        Retorna las noticias más recientes de ASOMAP
        """
        try:
            news = News.objects.filter(is_active=True).order_by('-fecha_publicacion')
            page = self.paginate_queryset(news)
            if page is not None:
                serializer = NewsSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': 'News not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'], url_path='promotions')
    def promotions(self, request):
        """
        Obtener promociones activas
        
        Retorna las promociones activas y vigentes de ASOMAP
        """
        try:
            promotions = Promotion.objects.filter(is_active=True).order_by('-fecha_inicio')
            page = self.paginate_queryset(promotions)
            if page is not None:
                serializer = PromotionSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = PromotionSerializer(promotions, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': 'Promotions not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )