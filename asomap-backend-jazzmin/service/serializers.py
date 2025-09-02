from rest_framework import serializers
from typing import Optional, List
from .models import ServicesPage, ServiceInfo


class ServiceInfoSerializer(serializers.ModelSerializer):
    """Serializer para información detallada de servicios"""
    image_url = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ServiceInfo
        fields = [
            'id', 'title', 'description', 'steps', 
            'image_url', 'image_alt', 'pdf_url'
        ]
    
    def get_image_url(self, obj) -> Optional[str]:
        return obj.image_url
    
    def get_pdf_url(self, obj) -> Optional[str]:
        """Retorna la URL del PDF (archivo o URL externa)"""
        if obj.pdf_url:
            return obj.pdf_url
        elif obj.pdf_file_url:
            return obj.pdf_file_url
        return None
    
    def get_steps(self, obj) -> str:
        """Retorna los pasos como HTML"""
        return obj.steps if obj.steps else ""


class ServicesPageSerializer(serializers.ModelSerializer):
    """Serializer para la página de servicios"""
    items = serializers.SerializerMethodField()
    item_details = ServiceInfoSerializer(many=True, read_only=True)
    
    class Meta:
        model = ServicesPage
        fields = [
            'id', 'title', 'subtitle', 'search_placeholder',
            'no_results_text', 'internet_banking_url', 'internet_banking_button',
            'items', 'item_details', 'is_active', 'created_at', 'updated_at'
        ]
    
    def get_items(self, obj) -> List[str]:
        """Obtener lista de títulos de servicios para búsqueda"""
        return [service.title for service in obj.item_details.filter(is_active=True)]
