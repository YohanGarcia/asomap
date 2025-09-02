"""
Comando de gestión para debuggear el contenido HTML de las noticias
"""
from django.core.management.base import BaseCommand
from news.models import News


class Command(BaseCommand):
    help = 'Debuggear el contenido HTML de las noticias'

    def handle(self, *args, **options):
        self.stdout.write('Debuggeando contenido HTML de las noticias...')
        
        # Obtener todas las noticias
        all_news = News.objects.all()
        
        for news in all_news:
            self.stdout.write(f'\n=== NOTICIA ID: {news.id} ===')
            self.stdout.write(f'Título: {news.title}')
            self.stdout.write(f'Contenido HTML:')
            self.stdout.write('-' * 50)
            self.stdout.write(news.full_content)
            self.stdout.write('-' * 50)
            
            # También mostrar el contenido parseado
            from news.serializers import NewsSerializer
            from rest_framework.test import APIRequestFactory
            
            factory = APIRequestFactory()
            request = factory.get('/')
            serializer = NewsSerializer(news, context={'request': request})
            
            self.stdout.write(f'Contenido parseado:')
            self.stdout.write(str(serializer.data.get('full_content', [])))
            self.stdout.write('=' * 50)
