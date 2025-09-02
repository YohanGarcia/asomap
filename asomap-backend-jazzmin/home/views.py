from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import DebitCardPromo, EducationItem, EducationSection, PeKeAccountSummary, Product, ProductSection, SliderItem
from .serializers import (
    DebitCardPromoSerializer, 
    EducationItemSerializer, 
    EducationSectionSerializer,
    EducationSectionCompleteSerializer,
    PeKeAccountSummarySerializer,
    ProductSerializer,
    ProductSectionSerializer,
    ProductSectionCompleteSerializer,
    SliderItemSerializer
)


class HomeViewSet(viewsets.ModelViewSet):
    """
    ViewSet para la página de inicio
    """
    queryset = DebitCardPromo.objects.all()
    serializer_class = DebitCardPromoSerializer
    
    @extend_schema(
        summary="Obtener promoción de tarjeta de débito",
        description="Retorna la promoción activa de tarjeta de débito para la página de inicio",
        responses={200: DebitCardPromoSerializer, 404: None},
        tags=['home']
    )
    @action(detail=False, methods=['get'], url_path='debit-card-promo')
    def debit_card_promo(self, request):
        """
        Obtener promoción de tarjeta de débito
        
        Retorna la promoción activa de tarjeta de débito para la página de inicio
        """
        try:
            promo = DebitCardPromo.objects.filter(is_active=True).first()
            if not promo:
                return Response(
                    {
                        'error': 'Debit card promotion not found',
                        'debug_info': {
                            'active_promos_count': DebitCardPromo.objects.filter(is_active=True).count(),
                            'total_promos_count': DebitCardPromo.objects.count()
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = self.get_serializer(promo)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {
                    'error': 'Debit card promotion not found',
                    'debug_info': {
                        'exception': str(e),
                        'active_promos_count': DebitCardPromo.objects.filter(is_active=True).count(),
                        'total_promos_count': DebitCardPromo.objects.count()
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(
        summary="Obtener sección de educación",
        description="Retorna la sección de educación activa con elementos educativos",
        responses={200: EducationSectionCompleteSerializer, 404: None},
        tags=['home']
    )
    @action(detail=False, methods=['get'], url_path='education-section')
    def education_section(self, request):
        """
        Obtener sección de educación
        
        Retorna la sección de educación activa con elementos educativos
        que coincide con la estructura esperada por el frontend
        """
        try:
            section = EducationSection.objects.filter(is_active=True).prefetch_related(
                'education_items'
            ).first()
            
            if not section:
                return Response(
                    {
                        'error': 'Education section not found',
                        'debug_info': {
                            'active_sections_count': EducationSection.objects.filter(is_active=True).count(),
                            'total_sections_count': EducationSection.objects.count(),
                            'total_items_count': EducationItem.objects.count()
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Preparar la respuesta que coincide con la estructura del frontend
            education_items = []
            for item in section.education_items.filter(is_active=True).order_by('order'):
                education_items.append({
                    'image': item.image_url,
                    'alt': item.alt,
                    'description': item.description
                })
            
            response_data = {
                'data': {
                    'title': section.title,
                    'subtitle': section.subtitle,
                    'educationItems': education_items,
                    'footerText': section.footer_text
                }
            }
            
            return Response(response_data)
            
        except Exception as e:
            return Response(
                {
                    'error': 'Education section not found',
                    'debug_info': {
                        'exception': str(e),
                        'active_sections_count': EducationSection.objects.filter(is_active=True).count(),
                        'total_sections_count': EducationSection.objects.count(),
                        'total_items_count': EducationItem.objects.count()
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(
        summary="Obtener resumen de cuenta PeKe",
        description="Retorna el resumen activo de cuenta PeKe para la página de inicio",
        responses={200: PeKeAccountSummarySerializer, 404: None},
        tags=['home']
    )
    @action(detail=False, methods=['get'], url_path='peke-account-summary')
    def peke_account_summary(self, request):
        """
        Obtener resumen de cuenta PeKe
        
        Retorna el resumen activo de cuenta PeKe para la página de inicio
        """
        try:
            summary = PeKeAccountSummary.objects.filter(is_active=True).first()
            if not summary:
                return Response(
                    {
                        'error': 'PeKe account summary not found',
                        'debug_info': {
                            'active_summaries_count': PeKeAccountSummary.objects.filter(is_active=True).count(),
                            'total_summaries_count': PeKeAccountSummary.objects.count()
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = PeKeAccountSummarySerializer(summary)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {
                    'error': 'PeKe account summary not found',
                    'debug_info': {
                        'exception': str(e),
                        'active_summaries_count': PeKeAccountSummary.objects.filter(is_active=True).count(),
                        'total_summaries_count': PeKeAccountSummary.objects.count()
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(
        summary="Obtener sección de productos",
        description="Retorna la sección de productos activa con productos",
        responses={200: ProductSectionCompleteSerializer, 404: None},
        tags=['home']
    )
    @action(detail=False, methods=['get'], url_path='product-section')
    def product_section(self, request):
        """
        Obtener sección de productos
        
        Retorna la sección de productos activa con productos
        que coincide con la estructura esperada por el frontend
        """
        try:
            section = ProductSection.objects.filter(is_active=True).prefetch_related(
                'products'
            ).first()
            
            if not section:
                return Response(
                    {
                        'error': 'Product section not found',
                        'debug_info': {
                            'active_sections_count': ProductSection.objects.filter(is_active=True).count(),
                            'total_sections_count': ProductSection.objects.count(),
                            'total_products_count': Product.objects.count()
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Preparar la respuesta que coincide con la estructura del frontend
            products = []
            for product in section.products.filter(is_active=True).order_by('order'):
                products.append({
                    'id': str(product.id),
                    'title': product.title,
                    'description': product.description,
                    'image': product.image_url,
                    'category': product.category,
                    'imageWidth': product.image_width,
                    'imageHeight': product.image_height
                })
            
            response_data = {
                'data': {
                    'section': {
                        'title': section.title,
                        'subtitle': section.subtitle
                    },
                    'buttonText': section.button_text,
                    'products': products
                }
            }
            
            return Response(response_data)
            
        except Exception as e:
            return Response(
                {
                    'error': 'Product section not found',
                    'debug_info': {
                        'exception': str(e),
                        'active_sections_count': ProductSection.objects.filter(is_active=True).count(),
                        'total_sections_count': ProductSection.objects.count(),
                        'total_products_count': Product.objects.count()
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @extend_schema(
        summary="Obtener elementos del slider",
        description="Retorna todos los elementos activos del slider ordenados",
        responses={200: SliderItemSerializer(many=True), 404: None},
        tags=['home']
    )
    @action(detail=False, methods=['get'], url_path='slider')
    def slider(self, request):
        """
        Obtener elementos del slider
        
        Retorna todos los elementos activos del slider ordenados
        que coincide con la estructura esperada por el frontend
        """
        try:
            slider_items = SliderItem.objects.filter(is_active=True).order_by('order')
            
            if not slider_items.exists():
                return Response(
                    {
                        'error': 'Slider items not found',
                        'debug_info': {
                            'active_items_count': SliderItem.objects.filter(is_active=True).count(),
                            'total_items_count': SliderItem.objects.count()
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Preparar la respuesta que coincide con la estructura del frontend
            slides = []
            for item in slider_items:
                slides.append({
                    'id': item.id,
                    'image': item.image_desktop_url,
                    'imageTablet': item.image_tablet_url,
                    'imageMobile': item.image_mobile_url,
                    'alt': item.alt
                })
            
            return Response(slides)
            
        except Exception as e:
            return Response(
                {
                    'error': 'Slider items not found',
                    'debug_info': {
                        'exception': str(e),
                        'active_items_count': SliderItem.objects.filter(is_active=True).count(),
                        'total_items_count': SliderItem.objects.count()
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )
