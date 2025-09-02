from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from prousuario.models import AccountType, AbandonedAccountsSection, YearlyDocument


class Command(BaseCommand):
    help = 'Crea datos de muestra para cuentas abandonadas e inactivas'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de muestra para cuentas abandonadas...')
        
        # Crear tipos de cuenta
        abandoned_type, created = AccountType.objects.get_or_create(
            label='Cuentas Abandonadas',
            defaults={
                'description': 'Cuentas sin movimientos por más de 10 años',
                'is_active': True
            }
        )
        
        inactive_type, created = AccountType.objects.get_or_create(
            label='Cuentas Inactivas',
            defaults={
                'description': 'Cuentas sin movimientos por más de 3 años',
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✓ Tipos de cuenta creados: {abandoned_type.label}, {inactive_type.label}')
        else:
            self.stdout.write(f'✓ Tipos de cuenta ya existían')
        
        # Crear sección principal
        section, created = AbandonedAccountsSection.objects.get_or_create(
            title='Cuentas Abandonadas e Inactivas',
            defaults={
                'description': 'Consulta el listado de cuentas abandonadas e inactivas por año',
                'is_active': True
            }
        )
        
        # Asociar tipos de cuenta a la sección
        section.account_types.add(abandoned_type, inactive_type)
        
        if created:
            self.stdout.write(f'✓ Sección creada: {section.title}')
        else:
            self.stdout.write(f'✓ Sección ya existía')
        
        # Nota: Los documentos YearlyDocument requieren archivos PDF obligatorios
        # Por ahora solo creamos la estructura básica
        self.stdout.write('⚠️  Nota: Los documentos YearlyDocument requieren archivos PDF')
        self.stdout.write('📝 Los documentos se pueden crear manualmente desde el admin')
        
        documents_created = 0
        self.stdout.write(self.style.SUCCESS('¡Datos de muestra creados exitosamente!'))
        
        # Mostrar resumen
        self.stdout.write('\nResumen:')
        self.stdout.write(f'- Tipos de cuenta: {AccountType.objects.count()}')
        self.stdout.write(f'- Secciones: {AbandonedAccountsSection.objects.count()}')
        self.stdout.write(f'- Documentos: {YearlyDocument.objects.count()}')
