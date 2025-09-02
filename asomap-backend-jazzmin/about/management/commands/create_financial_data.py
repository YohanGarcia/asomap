"""
Comando de gestión para crear datos de ejemplo de estados financieros
"""
from django.core.management.base import BaseCommand
from about.models import FinancialDocument, FinancialStatementsConfig


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para estados financieros'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo para estados financieros...')
        
        try:
            # Crear documentos financieros de ejemplo para 2024
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Auditados 2024",
                year="2024",
                defaults={
                    'document_type': 'audited',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q1 2024",
                year="2024",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '1',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q2 2024",
                year="2024",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '2',
                    'is_active': True
                }
            )
            
            # Crear configuración de estados financieros
            config = FinancialStatementsConfig.objects.get_or_create(
                defaults={
                    'title': "Estados Financieros",
                    'description': "Consulta nuestros estados financieros auditados y trimestrales",
                    'is_active': True
                }
            )[0]
            
            # Crear documentos financieros de ejemplo para 2023
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Auditados 2023",
                year="2023",
                defaults={
                    'document_type': 'audited',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q1 2023",
                year="2023",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '1',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q2 2023",
                year="2023",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '2',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q3 2023",
                year="2023",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '3',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q4 2023",
                year="2023",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '4',
                    'is_active': True
                }
            )
            
            # Crear documentos financieros de ejemplo para 2022
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Auditados 2022",
                year="2022",
                defaults={
                    'document_type': 'audited',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q1 2022",
                year="2022",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '1',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q2 2022",
                year="2022",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '2',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q3 2022",
                year="2022",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '3',
                    'is_active': True
                }
            )
            
            FinancialDocument.objects.get_or_create(
                title="Estados Financieros Q4 2022",
                year="2022",
                defaults={
                    'document_type': 'quarterly',
                    'quarter': '4',
                    'is_active': True
                }
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    '✅ Datos de estados financieros creados exitosamente:\n'
                    f'  - 1 configuración de estados financieros\n'
                    f'  - 3 años de documentos (2022, 2023, 2024)\n'
                    f'  - 3 documentos auditados\n'
                    f'  - 10 documentos trimestrales\n'
                    f'  - Total: 13 documentos financieros'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear datos de estados financieros: {e}')
            )
