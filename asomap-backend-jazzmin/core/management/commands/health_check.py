from django.core.management.base import BaseCommand
from django.db import connection
from django.core.cache import cache
from django.conf import settings
import psutil
import os
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Verificar la salud del sistema ASOMAP'

    def add_arguments(self, parser):
        parser.add_argument(
            '--detailed',
            action='store_true',
            help='Mostrar información detallada',
        )
        parser.add_argument(
            '--check-db',
            action='store_true',
            help='Verificar solo la base de datos',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🏥 Verificando salud del sistema ASOMAP...')
        )

        checks_passed = 0
        total_checks = 0

        # 1. Verificar base de datos
        if not options['check_db'] or options['check_db']:
            total_checks += 1
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    self.stdout.write(self.style.SUCCESS('✓ Base de datos: Conectada'))
                    checks_passed += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Base de datos: Error - {e}'))

        # 2. Verificar cache
        if not options['check_db']:
            total_checks += 1
            try:
                cache.set('health_check', 'ok', 10)
                if cache.get('health_check') == 'ok':
                    self.stdout.write(self.style.SUCCESS('✓ Cache: Funcionando'))
                    checks_passed += 1
                else:
                    self.stdout.write(self.style.WARNING('⚠️ Cache: No responde correctamente'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Cache: Error - {e}'))

        # 3. Verificar directorios
        if not options['check_db']:
            total_checks += 1
            required_dirs = ['media', 'static', 'logs']
            missing_dirs = []
            
            for directory in required_dirs:
                if not os.path.exists(directory):
                    missing_dirs.append(directory)
            
            if not missing_dirs:
                self.stdout.write(self.style.SUCCESS('✓ Directorios: Todos existen'))
                checks_passed += 1
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠️ Directorios: Faltan {", ".join(missing_dirs)}')
                )

        # 4. Verificar aplicaciones
        if not options['check_db']:
            total_checks += 1
            try:
                from django.apps import apps
                apps.check_apps_ready()
                self.stdout.write(self.style.SUCCESS('✓ Aplicaciones: Configuradas correctamente'))
                checks_passed += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Aplicaciones: Error - {e}'))

        # 5. Verificar configuración
        if not options['check_db']:
            total_checks += 1
            try:
                from django.core.management import execute_from_command_line
                execute_from_command_line(['manage.py', 'check', '--deploy'])
                self.stdout.write(self.style.SUCCESS('✓ Configuración: Válida para producción'))
                checks_passed += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️ Configuración: {e}'))

        # 6. Información del sistema (solo si detailed)
        if options['detailed'] and not options['check_db']:
            self.stdout.write('\n📊 Información del sistema:')
            
            # Uso de memoria
            memory = psutil.virtual_memory()
            self.stdout.write(f'  Memoria: {memory.percent}% usado')
            
            # Uso de disco
            disk = psutil.disk_usage('/')
            self.stdout.write(f'  Disco: {disk.percent}% usado')
            
            # CPU
            cpu_percent = psutil.cpu_percent(interval=1)
            self.stdout.write(f'  CPU: {cpu_percent}% usado')

        # Resumen
        self.stdout.write('\n�� Resumen:')
        self.stdout.write(f'  Checks pasados: {checks_passed}/{total_checks}')
        
        if checks_passed == total_checks:
            self.stdout.write(self.style.SUCCESS('�� Sistema saludable!'))
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️ Sistema con problemas ({checks_passed}/{total_checks} checks pasados)')
            ) 