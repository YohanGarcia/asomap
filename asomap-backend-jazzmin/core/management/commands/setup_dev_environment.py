from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Configurar entorno de desarrollo para ASOMAP'

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-migrations',
            action='store_true',
            help='Saltar la ejecución de migraciones',
        )
        parser.add_argument(
            '--skip-fixtures',
            action='store_true',
            help='Saltar la carga de datos iniciales',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forzar la ejecución sin confirmaciones',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🚀 Configurando entorno de desarrollo ASOMAP...')
        )

        if not options['force']:
            confirm = input('¿Continuar con la configuración? (y/N): ')
            if confirm.lower() != 'y':
                self.stdout.write(self.style.WARNING('Configuración cancelada.'))
                return

        try:
            # 1. Verificar configuración
            self.stdout.write('📋 Verificando configuración...')
            call_command('check', verbosity=0)
            self.stdout.write(self.style.SUCCESS('✓ Configuración válida'))

            # 2. Ejecutar migraciones
            if not options['skip_migrations']:
                self.stdout.write('🗄️ Ejecutando migraciones...')
                call_command('makemigrations', verbosity=0)
                call_command('migrate', verbosity=0)
                self.stdout.write(self.style.SUCCESS('✓ Migraciones completadas'))

            # 3. Crear directorios necesarios
            self.stdout.write('📁 Creando directorios...')
            directories = [
                'media',
                'static',
                'logs',
                'backups',
                'media/about/hero',
                'media/about/quienes-somos',
                'media/about/historia',
                'media/about/directores',
                'media/products/accounts',
                'media/products/loans',
                'media/products/cards',
                'media/products/certificates',
                'media/news',
                'media/promotions',
            ]
            
            for directory in directories:
                os.makedirs(directory, exist_ok=True)
                self.stdout.write(f'  ✓ {directory}')

            # 4. Cargar datos iniciales
            if not options['skip_fixtures']:
                self.stdout.write('📊 Cargando datos iniciales...')
                try:
                    call_command('create_about_data', verbosity=0)
                    call_command('create_products', verbosity=0)
                    call_command('create_sample_news', verbosity=0)
                    self.stdout.write(self.style.SUCCESS('✓ Datos iniciales cargados'))
                except Exception as e:
                    self.stdout.write(
                        self.style.WARNING(f'⚠️ Error cargando datos: {e}')
                    )

            # 5. Crear superusuario si no existe
            self.stdout.write('👤 Verificando superusuario...')
            from django.contrib.auth.models import User
            if not User.objects.filter(is_superuser=True).exists():
                self.stdout.write('Creando superusuario...')
                call_command('createsuperuser', interactive=False, verbosity=0)
                self.stdout.write(self.style.SUCCESS('✓ Superusuario creado'))
            else:
                self.stdout.write(self.style.SUCCESS('✓ Superusuario ya existe'))

            self.stdout.write(
                self.style.SUCCESS('🎉 Entorno de desarrollo configurado exitosamente!')
            )
            self.stdout.write('�� Próximos pasos:')
            self.stdout.write('  1. Ejecutar: python manage.py runserver')
            self.stdout.write('  2. Acceder a: http://localhost:8000/admin/')
            self.stdout.write('  3. Acceder a: http://localhost:8000/api/v1/')

        except Exception as e:
            logger.error(f'Error en setup_dev_environment: {e}')
            self.stdout.write(
                self.style.ERROR(f'❌ Error durante la configuración: {e}')
            )
            raise 