"""
Comando de gestión para crear banner de ejemplo
"""
from django.core.management.base import BaseCommand
from products.models import Banner


class Command(BaseCommand):
    help = 'Crea banner de ejemplo para el frontend'

    def handle(self, *args, **options):
        self.stdout.write('Creando banner de ejemplo...')
        
        # Datos del banner
        banner_data = {
            'title': '¿Listo para solicitar tu préstamo?',
            'description': 'Nuestro equipo está listo para ayudarte a hacer realidad tus proyectos financieros',
            'button1_name': 'Solicitar Préstamo',
            'button1_url': '/products/loans',
            'button2_name': 'Ver Otros Productos',
            'button2_url': '/products',
            'is_active': True,
            'order': 1
        }
        
        # Crear el banner solo si no existe ninguno
        if Banner.objects.exists():
            self.stdout.write(f'⚠️  Ya existe un banner en el sistema, saltando...')
            return
        
        banner = Banner.objects.create(**banner_data)
        created = True
        
        if created:
            self.stdout.write(f'✓ Banner "{banner_data["title"]}" creado exitosamente')
            self.stdout.write(f'  ✓ Botón 1: {banner_data["button1_name"]} -> {banner_data["button1_url"]}')
            self.stdout.write(f'  ✓ Botón 2: {banner_data["button2_name"]} -> {banner_data["button2_url"]}')
        else:
            self.stdout.write(f'⚠️  Banner "{banner_data["title"]}" ya existe, saltando...')
        
        self.stdout.write(
            self.style.SUCCESS(
                '✅ Banner de ejemplo procesado exitosamente'
            )
        )
