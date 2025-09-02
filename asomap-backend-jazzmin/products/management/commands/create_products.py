from django.core.management.base import BaseCommand
from products.models import Account, Loan, Card, Certificate
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Crear productos iniciales de ASOMAP'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forzar la creación aunque ya existan productos',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🏦 Creando productos iniciales...')
        )

        try:
            # 1. Cuentas
            accounts_data = [
                {
                    'title': 'Cuenta Clásica',
                    'description': 'La cuenta de ahorros tradicional de ASOMAP.',
                    'category': 'savings',
                    'features': [
                        'Sin comisión de mantenimiento',
                        'Interés compuesto mensual',
                        'Acceso a cajeros automáticos',
                        'Banca en línea disponible'
                    ]
                },
                {
                    'title': 'Cuenta Pekes',
                    'description': 'Cuenta especial para niños y jóvenes.',
                    'category': 'savings',
                    'features': [
                        'Edad mínima: 0 años',
                        'Interés especial para menores',
                        'Libreta de ahorros personalizada',
                        'Programa educativo de finanzas'
                    ]
                },
                {
                    'title': 'Cuenta Corriente',
                    'description': 'Cuenta corriente para transacciones diarias.',
                    'category': 'checking',
                    'features': [
                        'Cheques sin cargo',
                        'Banca en línea',
                        'Pagos automáticos',
                        'Tarjeta de débito incluida'
                    ]
                }
            ]

            for account_data in accounts_data:
                account, created = Account.objects.get_or_create(
                    title=account_data['title'],
                    defaults={
                        'description': account_data['description'],
                        'category': account_data['category'],
                        'features': account_data['features'],
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write(f'✓ Cuenta "{account_data["title"]}" creada')

            # 2. Préstamos
            loans_data = [
                {
                    'title': 'Préstamo de Consumo',
                    'description': 'Préstamo personal para necesidades inmediatas.',
                    'loan_type': 'personal',
                    'requirements': [
                        'Ser asociado activo por mínimo 6 meses',
                        'Ingresos comprobables',
                        'Documentos de identidad vigentes'
                    ]
                },
                {
                    'title': 'Préstamo Hipotecario',
                    'description': 'Financiamiento para vivienda con las mejores condiciones.',
                    'loan_type': 'mortgage',
                    'requirements': [
                        'Ser asociado activo por mínimo 1 año',
                        'Ingresos estables y comprobables',
                        'Avalúo de la propiedad'
                    ]
                },
                {
                    'title': 'Préstamo Comercial',
                    'description': 'Financiamiento para empresas y comercios.',
                    'loan_type': 'business',
                    'requirements': [
                        'Empresa registrada y operativa',
                        'Estados financieros actualizados',
                        'Plan de negocio'
                    ]
                }
            ]

            for loan_data in loans_data:
                loan, created = Loan.objects.get_or_create(
                    title=loan_data['title'],
                    defaults={
                        'description': loan_data['description'],
                        'loan_type': loan_data['loan_type'],
                        'requirements': loan_data['requirements'],
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write(f'✓ Préstamo "{loan_data["title"]}" creado')

            # 3. Tarjetas
            cards_data = [
                {
                    'title': 'Tarjeta de Débito ASOMAP',
                    'description': 'Tarjeta de débito con seguridad y conveniencia.',
                    'features': [
                        'Sin costo anual',
                        'Acceso a cajeros automáticos 24/7',
                        'Pagos en línea seguros',
                        'Notificaciones de transacciones'
                    ]
                },
                {
                    'title': 'Tarjeta de Crédito ASOMAP',
                    'description': 'Tarjeta de crédito con beneficios exclusivos.',
                    'features': [
                        'Programa de recompensas',
                        'Seguro de compras',
                        'Protección de viajes',
                        'Línea de crédito flexible'
                    ]
                }
            ]

            for card_data in cards_data:
                card, created = Card.objects.get_or_create(
                    title=card_data['title'],
                    defaults={
                        'description': card_data['description'],
                        'features': card_data['features'],
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write(f'✓ Tarjeta "{card_data["title"]}" creada')

            # 4. Certificados
            certificates_data = [
                {
                    'title': 'Certificado Financiero Clásico',
                    'description': 'Certificado de depósito a plazo fijo con tasas competitivas.',
                    'certificate_type': 'financial',
                    'investment_details': 'Plazo mínimo 30 días, Monto mínimo RD$ 10,000, Interés compuesto mensual, Sin comisiones por mantenimiento'
                },
                {
                    'title': 'Certificado Premium',
                    'description': 'Certificado de alto rendimiento para inversores.',
                    'certificate_type': 'investment',
                    'investment_details': 'Plazo mínimo 6 meses, Monto mínimo RD$ 50,000, Interés compuesto mensual, Beneficios exclusivos para clientes premium'
                }
            ]

            for cert_data in certificates_data:
                certificate, created = Certificate.objects.get_or_create(
                    title=cert_data['title'],
                    defaults={
                        'description': cert_data['description'],
                        'certificate_type': cert_data['certificate_type'],
                        'investment_details': cert_data['investment_details'],
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write(f'✓ Certificado "{cert_data["title"]}" creado')

            self.stdout.write(
                self.style.SUCCESS('🎉 Productos iniciales creados exitosamente!')
            )

        except Exception as e:
            logger.error(f'Error creando productos: {e}')
            self.stdout.write(
                self.style.ERROR(f'❌ Error creando productos: {e}')
            )
            raise 