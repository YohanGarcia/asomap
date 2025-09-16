"""
Comando de gestión para crear préstamos hipotecarios de ejemplo
"""
from django.core.management.base import BaseCommand
from products.models import Loan


class Command(BaseCommand):
    help = 'Crea préstamos hipotecarios de ejemplo para el frontend'

    def handle(self, *args, **options):
        self.stdout.write('Creando préstamos hipotecarios de ejemplo...')
        
        loans_data = [
            {
                'title': 'Compra de vivienda',
                'description': 'Financia la compra de tu vivienda con las mejores condiciones del mercado.',
                'loan_type': 'home_purchase',
                'details': [
                    'Financiamiento máximo de hasta del 80% del inmueble, incluye gastos legales.',
                    'Plazo de hasta 20 años.',
                    'Tasa de interés preferencial.',
                    'Aceptamos distintos comprobantes de ingresos.',
                    'Ingresos mínimos requeridos del grupo familiar de $600.00, durante el plazo del crédito'
                ]
            },
            {
                'title': 'Ampliación o remodelación',
                'description': 'Amplía o remodela tu vivienda actual con nuestro crédito hipotecario.',
                'loan_type': 'remodelation',
                'details': [
                    'Hasta el 100% del presupuesto de la obra, sin exceder del 80% del valor comercial del inmueble.',
                    'Plazo de hasta 20 años.',
                    'Aceptamos distintos comprobantes de ingresos.',
                    'Tasa de interés preferencial.'
                ]
            },
            {
                'title': 'Contrucción',
                'description': 'Construye tu vivienda desde cero con nuestro crédito hipotecario.',
                'loan_type': 'construction',
                'details': [
                    'Construye tu vivienda con un crédito hipotecario.',
                    'Financiamiento de hasta el 70% del valor del proyecto.',
                    'Plazo de hasta 20 años.',
                    'Tasa de interés preferencial en función del monto de la obra.',
                    'Aceptamos distintos comprobantes de ingresos.',
                    'Ingresos mínimos requeridos del grupo familiar de $600.00, durante el plazo del crédito.',
                    'Forma de pago: desembolsos según el avance de la obra.'
                ]
            },
            {
                'title': 'Compra de terreno',
                'description': 'Adquiere el terreno para construir tu vivienda con las mejores condiciones.',
                'loan_type': 'land_purchase',
                'details': [
                    'Adquiere el terreno para construir tu vivienda',
                    'Financiamiento máximo de hasta el 70% del valor del terreno.',
                    'Plazo de hasta 15 años.',
                    'Aceptamos distintos comprobantes de ingresos.',
                    'Tasa de interés preferencial.'
                ]
            }
        ]
        
        # Requisitos generales para todos los préstamos
        requirements_title = "Requisitos para Crédito Hipotecario"
        requirements = [
            "Para adquirir un Crédito Hipotecario:",
            "Ser mayor de 21 años.",
            "Ingreso mínimo de $600 del grupo familiar durante el plazo del crédito.",
            "Estabilidad laboral.",
            "Buen récord crediticio."
        ]
        
        created_count = 0
        for loan_item in loans_data:
            loan, created = Loan.objects.get_or_create(
                title=loan_item['title'],
                defaults={
                    'description': loan_item['description'],
                    'loan_type': loan_item['loan_type'],
                    'details': ' / '.join(loan_item['details']),
                    'requirements_title': requirements_title,
                    'requirements': ' / '.join(requirements),
                    'is_active': True
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(f'✓ Préstamo "{loan_item["title"]}" creado')
                self.stdout.write(f'  ✓ {len(loan_item["details"])} detalles agregados')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} préstamos hipotecarios de ejemplo creados exitosamente'
            )
        )
