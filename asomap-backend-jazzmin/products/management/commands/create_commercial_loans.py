"""
Comando de gestión para crear préstamos comerciales
"""
from django.core.management.base import BaseCommand
from products.models import Loan


class Command(BaseCommand):
    help = 'Crea préstamos comerciales para el frontend'

    def handle(self, *args, **options):
        self.stdout.write('Creando préstamos comerciales...')
        
        # Datos del préstamo comercial
        commercial_loan_data = {
            'title': 'Préstamos Comercial',
            'description': 'Accede a la solución de financiamiento de capital de trabajo o inversión, que tu negocio necesita.',
            'loan_type': 'consumer',  # Usamos consumer como tipo base
            'details': [
                'Financiamiento estratégico: Gestiona el capital necesario para el crecimiento de tu empresa, adquisición de inventario o equipos.',
                'Garantías: Contamos con garantías que se ajustan a tus necesidades de financiamiento.',
                'Competitividad: Accede a tasas de interés competitivas que se ajustan al perfil de tu empresa y plazo de tu necesidad.',
                'Respaldo y cobertura: Cuenta con respaldo en todo momento. Estamos a tu servicio y presentes en todo el país.'
            ],
            'requirements_title': 'Para adquirir un Préstamos Comercial',
            'requirements': [
                '2 años de actividad comercial y económica para personas jurídicas',
                '1 año para personas naturales',
                'Sin días de atraso en el último mes'
            ]
        }
        
        # Crear o actualizar el préstamo comercial
        loan, created = Loan.objects.get_or_create(
            title=commercial_loan_data['title'],
            defaults={
                'description': commercial_loan_data['description'],
                'loan_type': commercial_loan_data['loan_type'],
                'details': ', '.join(commercial_loan_data['details']),
                'requirements_title': commercial_loan_data['requirements_title'],
                'requirements': ', '.join(commercial_loan_data['requirements']),
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'✅ Préstamo comercial "{commercial_loan_data["title"]}" creado exitosamente')
            )
            self.stdout.write(f'  ✓ {len(commercial_loan_data["details"])} beneficios agregados')
            self.stdout.write(f'  ✓ {len(commercial_loan_data["requirements"])} requisitos agregados')
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️ El préstamo comercial "{commercial_loan_data["title"]}" ya existe')
            )
