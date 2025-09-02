from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import SavingTip, SliderSlide, FAQItem
from .serializers import SavingTipSerializer, SliderSlideSerializer, FAQItemSerializer


# Create your views here.


class SavingTipViewSet(viewsets.ModelViewSet):
    """
    ViewSet para consejos de ahorro y educación financiera
    """
    queryset = SavingTip.objects.filter(is_active=True).order_by('order', 'id')
    serializer_class = SavingTipSerializer
    
    @extend_schema(
        summary="Listar consejos de ahorro",
        description="Retorna todos los consejos de ahorro activos ordenados por orden",
        responses={200: SavingTipSerializer(many=True)},
        tags=['financial-guidance']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Obtener consejo de ahorro",
        description="Retorna un consejo de ahorro específico por ID",
        responses={200: SavingTipSerializer, 404: None},
        tags=['financial-guidance']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class SliderSlideViewSet(viewsets.ModelViewSet):
    """
    ViewSet para slides del slider de educación financiera
    """
    queryset = SliderSlide.objects.filter(is_active=True).order_by('order', 'id')
    serializer_class = SliderSlideSerializer
    
    @extend_schema(
        summary="Listar slides del slider",
        description="Retorna todos los slides activos ordenados por orden",
        responses={200: SliderSlideSerializer(many=True)},
        tags=['financial-guidance']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Obtener slide del slider",
        description="Retorna un slide específico por ID",
        responses={200: SliderSlideSerializer, 404: None},
        tags=['financial-guidance']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class FAQItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet para preguntas frecuentes de educación financiera
    """
    queryset = FAQItem.objects.filter(is_active=True).order_by('order', 'id')
    serializer_class = FAQItemSerializer
    
    @extend_schema(
        summary="Listar preguntas frecuentes",
        description="Retorna todas las preguntas frecuentes activas ordenadas por orden",
        responses={200: FAQItemSerializer(many=True)},
        tags=['financial-guidance']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Obtener pregunta frecuente",
        description="Retorna una pregunta frecuente específica por ID",
        responses={200: FAQItemSerializer, 404: None},
        tags=['financial-guidance']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
