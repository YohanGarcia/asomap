"""
Comando de gestión para debuggear las promociones
"""
from django.core.management.base import BaseCommand
from news.models import Promotion


class Command(BaseCommand):
    help = 'Debuggear las promociones en la base de datos'

    def handle(self, *args, **options):
        self.stdout.write('Debuggeando promociones...')
        
        # Obtener todas las promociones
        all_promotions = Promotion.objects.all()
        self.stdout.write(f'Total de promociones encontradas: {all_promotions.count()}')
        
        for promotion in all_promotions:
            self.stdout.write(f'\n=== PROMOCIÓN ID: {promotion.id} ===')
            self.stdout.write(f'Título: {promotion.title}')
            self.stdout.write(f'Descripción: {promotion.description}')
            self.stdout.write(f'Categoría: {promotion.category}')
            self.stdout.write(f'Tags: {promotion.tags}')
            self.stdout.write(f'Términos: {promotion.terms}')
            self.stdout.write(f'Fecha inicio: {promotion.fecha_inicio}')
            self.stdout.write(f'Fecha fin: {promotion.fecha_fin}')
            self.stdout.write(f'Activa: {promotion.is_active}')
            self.stdout.write(f'Contenido completo: {promotion.full_content[:100]}...' if promotion.full_content else 'Sin contenido')
            
            # Probar las propiedades
            try:
                self.stdout.write(f'Tags list: {promotion.tags_list}')
                self.stdout.write(f'Terms list: {promotion.terms_list}')
                self.stdout.write(f'Valid until: {promotion.valid_until}')
            except Exception as e:
                self.stdout.write(f'Error en propiedades: {e}')
            
            # Probar el serializer
            try:
                from news.serializers import PromotionSerializer
                from rest_framework.test import APIRequestFactory
                
                factory = APIRequestFactory()
                request = factory.get('/')
                serializer = PromotionSerializer(promotion, context={'request': request})
                
                self.stdout.write(f'Serializer data: {serializer.data}')
            except Exception as e:
                self.stdout.write(f'Error en serializer: {e}')
            
            self.stdout.write('=' * 50)
