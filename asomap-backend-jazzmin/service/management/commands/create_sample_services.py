from django.core.management.base import BaseCommand
from service.models import ServicesPage, ServiceInfo


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para servicios bancarios'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo para servicios bancarios...')
        
        # Crear página de servicios con los datos exactos del frontend
        page, created = ServicesPage.objects.get_or_create(
            title='Servicios Bancarios',
            defaults={
                'subtitle': 'Descubre todos nuestros servicios disponibles para ti',
                'search_placeholder': 'Buscar servicios...',
                'no_results_text': 'No se encontraron servicios',
                'internet_banking_url': 'https://www.ibanking.asomap.com.do/onlinebanking',
                'internet_banking_button': 'Acceder a Banca en Línea',
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Página creada: {page.title}')
        else:
            self.stdout.write(f'🔄 Página actualizada: {page.title}')
        
        # Datos exactos del frontend
        services_data = [
            {
                'title': 'Autocaja',
                'description': 'Es un servicio que te permite realizar tus transacciones desde tu propio vehículo. Disponible en las sucursales de:',
                'steps': '''
                <ul>
                    <li>Oficina Principal</li>
                    <li>Cayetano Germosén</li>
                    <li>San Víctor</li>
                    <li>Licey al Medio</li>
                </ul>
                ''',
                'image_alt': 'Servicio de Autocaja',
                'order': 1
            },
            {
                'title': 'Pago impuestos DGII',
                'description': 'Paga todo los Impuestos de la DGII en nuestras oficina de la Asociación Mocana de Ahorros y Prestamos',
                'steps': '''
                <ol>
                    <li>Ingresa a tu cuenta en línea o visita una sucursal</li>
                    <li>Selecciona la opción de pago de impuestos DGII</li>
                    <li>Ingresa el número de referencia de tu declaración</li>
                    <li>Verifica los detalles y confirma el pago</li>
                </ol>
                ''',
                'image_alt': 'Pago de Impuestos DGII',
                'order': 2
            },
            {
                'title': 'Pago servicio de teléfono',
                'description': 'Paga tu factura de CLARO-CODETEL en nuestra oficina principal y cada una de nuestras sucursales, con un servicio personalizado de primera calidad.',
                'steps': '''
                <ol>
                    <li>Accede a tu banca en línea o móvil</li>
                    <li>Selecciona la opción de pago de servicios</li>
                    <li>Elige tu proveedor de servicio telefónico</li>
                    <li>Ingresa el número de cuenta o referencia</li>
                    <li>Confirma el monto y realiza el pago</li>
                </ol>
                ''',
                'image_alt': 'Pago de Servicio de Teléfono',
                'order': 3
            },
            {
                'title': 'Pago servicio de telecable',
                'description': 'Paga tu factura de Televiaducto S.A. en nuestra oficina principal y en nuestras sucursales de San Víctor, Juan López y Cayetano Germosén donde te esperamos para brindarte el mejor de los servicios.',
                'steps': '''
                <ol>
                    <li>Inicia sesión en tu cuenta bancaria en línea</li>
                    <li>Busca la sección de pagos de servicios</li>
                    <li>Selecciona tu proveedor de cable</li>
                    <li>Ingresa tu número de cuenta de cable</li>
                    <li>Verifica el monto y completa el pago</li>
                </ol>
                ''',
                'image_alt': 'Pago de Servicio de Telecable',
                'order': 4
            },
            {
                'title': 'Pago energía eléctrica',
                'description': 'Paga tu factura de EDENORTE en nuestra oficina principal y en cada una de nuestras sucursales con el mejor de los servicios.',
                'steps': '''
                <ol>
                    <li>Accede a nuestra plataforma de banca en línea</li>
                    <li>Navega hasta la sección de pago de servicios</li>
                    <li>Elige tu compañía eléctrica</li>
                    <li>Introduce el número de referencia de tu factura</li>
                    <li>Revisa los detalles y confirma el pago</li>
                </ol>
                ''',
                'image_alt': 'Pago de Energía Eléctrica',
                'order': 5
            },
            {
                'title': 'Depósito nocturno',
                'description': 'Es la facilidad que otorga la Asociación a sus clientes de depositar sus recursos en horario nocturno, sábado en la tarde, domingos y días feriados, con los mayores niveles de seguridad. Opera en la Oficina Principal y varias sucursales.',
                'steps': '''
                <ol>
                    <li>Prepara tu depósito en una bolsa de seguridad especial</li>
                    <li>Visita la ubicación del depósito nocturno más cercana</li>
                    <li>Utiliza tu tarjeta de acceso para abrir el buzón</li>
                    <li>Coloca la bolsa de depósito en el buzón</li>
                    <li>Asegúrate de que el buzón se cierre completamente</li>
                </ol>
                ''',
                'image_alt': 'Depósito Nocturno',
                'order': 6
            },
            {
                'title': 'Tarifario de productos y servicios',
                'description': 'Consulta nuestro tarifario actualizado de productos y servicios, donde encontrarás información detallada sobre tasas, comisiones y cargos.',
                'steps': '',
                'image_alt': 'Tarifario de Productos y Servicios',
                'order': 7,
                'pdf_url': 'https://www.asomap.com.do/wp-content/uploads/2024/04/Tarifario-actualizado-a-Marzo-2024.pdf'
            }
        ]
        
        created_count = 0
        updated_count = 0
        
        for service_data in services_data:
            # Preparar defaults con pdf_url si existe
            defaults = {
                'description': service_data['description'],
                'steps': service_data['steps'],
                'image_alt': service_data['image_alt'],
                'order': service_data['order'],
                'is_active': True
            }
            
            # Agregar pdf_url si existe
            if 'pdf_url' in service_data:
                defaults['pdf_url'] = service_data['pdf_url']
            
            service, service_created = ServiceInfo.objects.get_or_create(
                services_page=page,
                title=service_data['title'],
                defaults=defaults
            )
            
            if service_created:
                self.stdout.write(f'✅ Servicio creado: {service.title}')
                created_count += 1
            else:
                # Actualizar datos existentes
                service.description = service_data['description']
                service.steps = service_data['steps']
                service.image_alt = service_data['image_alt']
                service.order = service_data['order']
                service.is_active = True
                
                # Manejar PDF URL si existe
                if 'pdf_url' in service_data:
                    service.pdf_url = service_data['pdf_url']
                
                service.save()
                self.stdout.write(f'🔄 Servicio actualizado: {service.title}')
                updated_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Proceso completado. {created_count} servicios creados, {updated_count} actualizados.'
            )
        )
        
        # Mostrar resumen
        self.stdout.write('\n📋 Resumen de servicios creados:')
        for service in page.item_details.all().order_by('order'):
            self.stdout.write(f'  {service.order}. {service.title}')
