from django.core.management.base import BaseCommand
from core.email_utils import test_email_configuration


class Command(BaseCommand):
    help = 'Prueba la configuración de email activa'

    def add_arguments(self, parser):
        parser.add_argument(
            '--config-id',
            type=int,
            help='ID de la configuración específica a probar'
        )

    def handle(self, *args, **options):
        config_id = options.get('config_id')
        
        self.stdout.write(
            self.style.SUCCESS('Probando configuración de email...')
        )
        
        success, message = test_email_configuration(config_id)
        
        if success:
            self.stdout.write(
                self.style.SUCCESS(f'✅ {message}')
            )
        else:
            self.stdout.write(
                self.style.ERROR(f'❌ {message}')
            )
