"""
Comando de gestión para limpiar noticias duplicadas
"""
from django.core.management.base import BaseCommand
from news.models import News


class Command(BaseCommand):
    help = 'Limpia noticias duplicadas en la base de datos'

    def handle(self, *args, **options):
        self.stdout.write('Limpiando noticias duplicadas...')
        
        # Obtener todas las noticias
        all_news = News.objects.all()
        self.stdout.write(f'Total de noticias encontradas: {all_news.count()}')
        
        # Mostrar todas las noticias
        for news in all_news:
            self.stdout.write(f'- ID: {news.id}, Título: {news.title}, Creada: {news.created_at}')
        
        # Preguntar si quiere eliminar todas y recrear
        response = input('\n¿Quieres eliminar todas las noticias y recrear los datos de ejemplo? (s/n): ')
        
        if response.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            # Eliminar todas las noticias
            deleted_count = all_news.count()
            all_news.delete()
            self.stdout.write(f'✓ {deleted_count} noticias eliminadas')
            
            # Recrear datos de ejemplo
            self.stdout.write('Recreando datos de ejemplo...')
            from django.core.management import call_command
            call_command('create_sample_news')
            
            self.stdout.write(
                self.style.SUCCESS(
                    '✅ Limpieza completada exitosamente'
                )
            )
        else:
            self.stdout.write('Operación cancelada')
