from django.core.management.base import BaseCommand
from prousuario.models import ServiceRatesPage, ServiceCategory, ServiceRate


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para Service Rates'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo para Service Rates...')
        
        # Crear página principal
        page, created = ServiceRatesPage.objects.get_or_create(
            title="Tarifas de Servicios",
            defaults={
                'description': "Información detallada sobre las tarifas de nuestros servicios",
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Página creada: {page.title}')
        else:
            self.stdout.write(f'📄 Página existente: {page.title}')
        
        # Crear categoría "Servicios Básicos"
        category1, created = ServiceCategory.objects.get_or_create(
            name="Servicios Básicos",
            defaults={
                'order': 1,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Categoría creada: {category1.name}')
        else:
            self.stdout.write(f'📂 Categoría existente: {category1.name}')
        
        # Crear tarifas para Servicios Básicos
        rate1_1, created = ServiceRate.objects.get_or_create(
            category=category1,
            service="Apertura de Cuenta",
            defaults={
                'description': "Proceso de apertura de cuenta nueva",
                'rate': "RD$ 500.00",
                'details': """
                <ul>
                    <li>Incluye tarjeta de débito</li>
                    <li>Kit de bienvenida</li>
                    <li>Acceso a banca en línea</li>
                </ul>
                """,
                'order': 1,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Tarifa creada: {rate1_1.service}')
        else:
            self.stdout.write(f'💵 Tarifa existente: {rate1_1.service}')
        
        rate1_2, created = ServiceRate.objects.get_or_create(
            category=category1,
            service="Mantenimiento Mensual",
            defaults={
                'description': "Cargo por mantenimiento de cuenta",
                'rate': "RD$ 100.00",
                'details': """
                <ul>
                    <li>Aplica a cuentas de ahorro regular</li>
                    <li>Exento para cuentas premium</li>
                </ul>
                """,
                'order': 2,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Tarifa creada: {rate1_2.service}')
        else:
            self.stdout.write(f'💵 Tarifa existente: {rate1_2.service}')
        
        # Crear categoría "Servicios Electrónicos"
        category2, created = ServiceCategory.objects.get_or_create(
            name="Servicios Electrónicos",
            defaults={
                'order': 2,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Categoría creada: {category2.name}')
        else:
            self.stdout.write(f'📂 Categoría existente: {category2.name}')
        
        # Crear tarifas para Servicios Electrónicos
        rate2_1, created = ServiceRate.objects.get_or_create(
            category=category2,
            service="Transferencia Interbancaria",
            defaults={
                'description': "Transferencias a otros bancos",
                'rate': "RD$ 75.00",
                'details': """
                <ul>
                    <li>Procesamiento mismo día</li>
                    <li>Límite máximo RD$ 1,000,000.00</li>
                </ul>
                """,
                'order': 1,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Tarifa creada: {rate2_1.service}')
        else:
            self.stdout.write(f'💵 Tarifa existente: {rate2_1.service}')
        
        rate2_2, created = ServiceRate.objects.get_or_create(
            category=category2,
            service="Pago de Servicios",
            defaults={
                'description': "Pagos de servicios públicos",
                'rate': "Gratis",
                'details': """
                <ul>
                    <li>Luz, agua, teléfono</li>
                    <li>Sin comisión adicional</li>
                </ul>
                """,
                'order': 2,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Tarifa creada: {rate2_2.service}')
        else:
            self.stdout.write(f'💵 Tarifa existente: {rate2_2.service}')
        
        # Crear categoría "Tarjetas"
        category3, created = ServiceCategory.objects.get_or_create(
            name="Tarjetas",
            defaults={
                'order': 3,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Categoría creada: {category3.name}')
        else:
            self.stdout.write(f'📂 Categoría existente: {category3.name}')
        
        # Crear tarifas para Tarjetas
        rate3_1, created = ServiceRate.objects.get_or_create(
            category=category3,
            service="Reposición de Tarjeta",
            defaults={
                'description': "Reemplazo de tarjeta por pérdida o daño",
                'rate': "RD$ 300.00",
                'details': """
                <ul>
                    <li>Entrega en 3-5 días hábiles</li>
                    <li>Incluye nueva activación</li>
                </ul>
                """,
                'order': 1,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Tarifa creada: {rate3_1.service}')
        else:
            self.stdout.write(f'💵 Tarifa existente: {rate3_1.service}')
        
        rate3_2, created = ServiceRate.objects.get_or_create(
            category=category3,
            service="Avance de Efectivo",
            defaults={
                'description': "Retiro de efectivo con tarjeta de crédito",
                'rate': "6% del monto",
                'details': """
                <ul>
                    <li>Mínimo RD$ 300.00</li>
                    <li>Sujeto a disponibilidad</li>
                </ul>
                """,
                'order': 2,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Tarifa creada: {rate3_2.service}')
        else:
            self.stdout.write(f'💵 Tarifa existente: {rate3_2.service}')
        
        self.stdout.write(
            self.style.SUCCESS(
                '✅ Datos de ejemplo para Service Rates creados exitosamente!\n'
                '📝 Endpoint disponible: /api/user-support/service-rates/'
            )
        )
