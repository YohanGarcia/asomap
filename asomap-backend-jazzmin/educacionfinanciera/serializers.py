from rest_framework import serializers
from .models import SavingTip, SliderSlide, FAQItem


class SavingTipSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = SavingTip
        fields = [
            'id', 'title', 'description', 'content', 'link', 
            'order', 'is_active', 'created_at', 'updated_at'
        ]
    
    def get_content(self, obj):
        """Retorna el contenido HTML del ProseEditor"""
        if obj.content:
            return obj.content
        return ""


class SliderSlideSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = SliderSlide
        fields = [
            'id', 'image_url', 'title', 'description', 
            'order', 'is_active', 'created_at', 'updated_at'
        ]
    
    def get_image_url(self, obj):
        """Retorna la URL de la imagen"""
        return obj.image_url


class FAQItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQItem
        fields = [
            'id', 'question', 'answer', 'order', 
            'is_active', 'created_at', 'updated_at'
        ]
