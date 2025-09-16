from rest_framework import serializers
from .models import News, Promotion, NewsMedia
from bs4 import BeautifulSoup
import re


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    full_content = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    media = serializers.SerializerMethodField()
    related_links = serializers.SerializerMethodField()
    
    class Meta:
        model = News
        fields = [
            'id', 'image', 'title', 'description', 'date', 'author', 
            'category', 'tags', 'full_content', 'media', 'related_links'
        ]

    def get_image(self, obj):
        """Retorna la URL de la imagen"""
        if obj.image:
            return obj.image.url
        return None

    def get_date(self, obj):
        """Retorna la fecha formateada"""
        return obj.formatted_date

    def get_tags(self, obj):
        """Retorna las etiquetas como lista"""
        return obj.tags_list

    def get_media(self, obj):
        """Retorna los archivos de media como lista estructurada"""
        media_files = obj.media_files.filter(is_active=True).order_by('order', 'created_at')
        return [
            {
                'type': media.media_type,
                'url': media.file.url if media.file else None,
                'caption': media.caption or ''
            }
            for media in media_files
        ]

    def get_related_links(self, obj):
        """Retorna los enlaces relacionados como lista"""
        return obj.related_links_list

    def get_full_content(self, obj):
        """Convierte el contenido HTML de ProseEditor al formato estructurado del frontend"""
        if not obj.full_content:
            return []
        
        try:
            soup = BeautifulSoup(obj.full_content, 'html.parser')
            content = []
            
            # Procesar elementos en orden, evitando duplicados
            for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'blockquote', 'pre']):
                # Verificar que el elemento no sea hijo de una lista ya procesada
                if element.parent and element.parent.name in ['ul', 'ol']:
                    continue
                    
                if element.name == 'p':
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'paragraph',
                            'content': text
                        })
                elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'subtitle',
                            'content': text
                        })
                elif element.name in ['ul', 'ol']:
                    items = [li.get_text().strip() for li in element.find_all('li') if li.get_text().strip()]
                    if items:
                        content.append({
                            'type': 'list',
                            'content': items
                        })
                elif element.name == 'blockquote':
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'quote',
                            'content': text
                        })
                elif element.name == 'pre':
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'paragraph',
                            'content': text
                        })
            
            # Filtrar contenido duplicado
            filtered_content = []
            seen_content = set()
            
            for item in content:
                if item['type'] == 'list':
                    # Para listas, verificar si los elementos ya aparecieron como párrafos
                    list_items = set(item['content'])
                    if not any(item_text in seen_content for item_text in list_items):
                        filtered_content.append(item)
                        seen_content.update(list_items)
                else:
                    # Para otros tipos, verificar si el contenido ya apareció
                    if item['content'] not in seen_content:
                        filtered_content.append(item)
                        seen_content.add(item['content'])
            
            return filtered_content
        except Exception:
            # Si hay error en el parsing, retornar como párrafo simple
            return [{
                'type': 'paragraph',
                'content': obj.full_content
            }]


class PromotionSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    terms = serializers.SerializerMethodField()
    full_content = serializers.SerializerMethodField()
    media = serializers.SerializerMethodField()
    related_links = serializers.SerializerMethodField()
    validUntil = serializers.SerializerMethodField()
    
    class Meta:
        model = Promotion
        fields = [
            'id', 'image', 'title', 'description', 'category', 
            'tags', 'full_content', 'media', 'related_links', 'validUntil', 
            'terms', 'fecha_inicio', 'fecha_fin', 'is_active', 'created_at', 'updated_at'
        ]

    def get_image(self, obj):
        """Retorna la URL de la imagen"""
        return obj.image_url

    def get_tags(self, obj):
        """Retorna las etiquetas como lista"""
        return obj.tags_list

    def get_terms(self, obj):
        """Retorna los términos y condiciones como lista"""
        return obj.terms_list

    def get_media(self, obj):
        """Retorna las URLs de media como lista"""
        return obj.media_list

    def get_related_links(self, obj):
        """Retorna los enlaces relacionados como lista"""
        return obj.related_links_list

    def get_validUntil(self, obj):
        """Retorna la fecha de fin formateada"""
        return obj.valid_until

    def get_full_content(self, obj):
        """Convierte el contenido HTML de ProseEditor al formato estructurado del frontend"""
        if not obj.full_content:
            return []
        
        try:
            soup = BeautifulSoup(obj.full_content, 'html.parser')
            content = []
            
            # Procesar elementos en orden, evitando duplicados
            for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'blockquote', 'pre']):
                # Verificar que el elemento no sea hijo de una lista ya procesada
                if element.parent and element.parent.name in ['ul', 'ol']:
                    continue
                    
                if element.name == 'p':
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'paragraph',
                            'content': text
                        })
                elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'subtitle',
                            'content': text
                        })
                elif element.name in ['ul', 'ol']:
                    items = [li.get_text().strip() for li in element.find_all('li') if li.get_text().strip()]
                    if items:
                        content.append({
                            'type': 'list',
                            'content': items
                        })
                elif element.name == 'blockquote':
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'quote',
                            'content': text
                        })
                elif element.name == 'pre':
                    text = element.get_text().strip()
                    if text:
                        content.append({
                            'type': 'paragraph',
                            'content': text
                        })
            
            # Filtrar contenido duplicado
            filtered_content = []
            seen_content = set()
            
            for item in content:
                if item['type'] == 'list':
                    # Para listas, verificar si los elementos ya aparecieron como párrafos
                    list_items = set(item['content'])
                    if not any(item_text in seen_content for item_text in list_items):
                        filtered_content.append(item)
                        seen_content.update(list_items)
                else:
                    # Para otros tipos, verificar si el contenido ya apareció
                    if item['content'] not in seen_content:
                        filtered_content.append(item)
                        seen_content.add(item['content'])
            
            return filtered_content
        except Exception:
            # Si hay error en el parsing, retornar como párrafo simple
            return [{
                'type': 'paragraph',
                'content': obj.full_content
            }] 