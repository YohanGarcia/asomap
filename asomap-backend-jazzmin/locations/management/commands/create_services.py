"""
Comando de gestión para crear servicios predefinidos
"""
from django.core.management.base import BaseCommand
from locations.models import Service


class Command(BaseCommand):
    help = 'Crea servicios predefinidos para las ubicaciones'

    def handle(self, *args, **options):
        self.stdout.write('Creando servicios predefinidos...')
        
        services_data = [
            # todos los Servicios
            {'name': 'Todos los Servicios', 'description': 'Todos los Servicios disponibles'},
            # Servicios bancarios básicos
            {'name': 'Depósitos', 'description': 'Depósitos en efectivo y cheques'},
            {'name': 'Retiros', 'description': 'Retiros de efectivo'},
            {'name': 'Transferencias', 'description': 'Transferencias entre cuentas'},
            {'name': 'Pagos', 'description': 'Pago de servicios y facturas'},
            {'name': 'Consulta de saldo', 'description': 'Consulta de saldo de cuentas'},
            
            # Servicios de préstamos
            {'name': 'Solicitud de préstamos', 'description': 'Solicitud de préstamos personales y comerciales'},
            {'name': 'Pago de préstamos', 'description': 'Pago de cuotas de préstamos'},
            {'name': 'Microcréditos', 'description': 'Solicitud y pago de microcréditos'},
            
            # Servicios de tarjetas
            {'name': 'Emisión de tarjetas', 'description': 'Solicitud y emisión de tarjetas de débito y crédito'},
            {'name': 'Activación de tarjetas', 'description': 'Activación de tarjetas nuevas'},
            {'name': 'Bloqueo de tarjetas', 'description': 'Bloqueo temporal o permanente de tarjetas'},
            {'name': 'Cambio de PIN', 'description': 'Cambio de PIN de tarjetas'},
            
            # Servicios de cuentas
            {'name': 'Apertura de cuentas', 'description': 'Apertura de cuentas de ahorro y corrientes'},
            {'name': 'Cierre de cuentas', 'description': 'Cierre de cuentas bancarias'},
            {'name': 'Certificados bancarios', 'description': 'Emisión de certificados bancarios'},
            
            # Servicios especializados
            {'name': 'Cajero automático', 'description': 'Retiros y consultas en cajero automático'},
            {'name': 'Banca en línea', 'description': 'Asistencia para banca en línea'},
            {'name': 'Banca móvil', 'description': 'Asistencia para banca móvil'},
            {'name': 'Cambio de moneda', 'description': 'Compra y venta de divisas'},
            {'name': 'Giros', 'description': 'Envío y recepción de giros'},
            
            # Servicios empresariales
            {'name': 'Cuentas empresariales', 'description': 'Servicios para empresas'},
            {'name': 'Préstamos comerciales', 'description': 'Préstamos para negocios'},
            {'name': 'Facturación', 'description': 'Servicios de facturación'},
            {'name': 'Nómina', 'description': 'Servicios de nómina empresarial'},
            
            # Servicios de inversión
            {'name': 'Inversiones', 'description': 'Asesoría en inversiones'},
            {'name': 'Fondos mutuos', 'description': 'Compra y venta de fondos mutuos'},
            {'name': 'Seguros', 'description': 'Contratación de seguros'},
            
            # Servicios de atención al cliente
            {'name': 'Atención al cliente', 'description': 'Atención personalizada al cliente'},
            {'name': 'Reclamos', 'description': 'Gestión de reclamos y sugerencias'},
            {'name': 'Asesoría financiera', 'description': 'Asesoría financiera personalizada'},
        ]
        
        created_count = 0
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                name=service_data['name'],
                defaults={
                    'description': service_data['description'],
                    'is_active': True
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'✓ Servicio "{service_data["name"]}" creado')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} servicios predefinidos creados exitosamente'
            )
        )
