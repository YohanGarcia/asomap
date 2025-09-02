"""
Comando de gestión para crear préstamos de consumo
"""
from django.core.management.base import BaseCommand
from products.models import Loan


class Command(BaseCommand):
    help = 'Crea préstamos de consumo para el frontend'

    def handle(self, *args, **options):
        self.stdout.write('Creando préstamos de consumo...')
        
        # Datos del préstamo de consumo
        consumer_loan_data = {
            'title': 'Préstamos de Consumo',
            'description': '¡Solicita ahora nuestro producto de financiamiento, el momento de cumplir tus sueños!',
            'loan_type': 'consumer',
            'details': [
                'Altamente adaptable: Ofrece montos y plazos ajustados a sus necesidades.',
                'Ágil y flexible: Obtén tu préstamo de manera rápida y flexible para ganar tiempo.',
                'Competitivo: Accede a una tasa de interés altamente competitiva.',
                'Respaldo y cobertura: Cuenta con cobertura del seguro de vida sobre saldo deudor.'
            ],
            'requirements_title': 'Adquiere un Préstamos de Consumo Requisitos',
            'requirements': [
                'Cédula de identidad y electoral o pasaporte (para extranjeros).',
                'Carta de trabajo.',
                'Tres últimos volantes de pago.'
            ]
        }
        
        # Crear o actualizar el préstamo de consumo
        loan, created = Loan.objects.get_or_create(
            title=consumer_loan_data['title'],
            defaults={
                'description': consumer_loan_data['description'],
                'loan_type': consumer_loan_data['loan_type'],
                'details': ', '.join(consumer_loan_data['details']),
                'requirements_title': consumer_loan_data['requirements_title'],
                'requirements': ', '.join(consumer_loan_data['requirements']),
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'✅ Préstamo de consumo "{consumer_loan_data["title"]}" creado exitosamente')
            )
            self.stdout.write(f'  ✓ {len(consumer_loan_data["details"])} beneficios agregados')
            self.stdout.write(f'  ✓ {len(consumer_loan_data["requirements"])} requisitos agregados')
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️ El préstamo de consumo "{consumer_loan_data["title"]}" ya existe')
            )
