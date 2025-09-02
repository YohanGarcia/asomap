"""
Comando de gestión para crear tarjetas de ejemplo
"""
import requests
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings
from products.models import Card, CardBenefit
from core.cloudinary_utils import is_cloudinary_configured, get_supported_formats


class Command(BaseCommand):
    help = 'Crea tarjetas de ejemplo para el frontend'

    def download_image(self, url, filename):
        """Descarga una imagen desde una URL y la guarda en el modelo"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Extraer la extensión del archivo de la URL
            file_extension = url.split('.')[-1].split('?')[0]
            supported_formats = get_supported_formats()
            if file_extension not in supported_formats:
                file_extension = 'jpg'  # Default a jpg si no se puede determinar
            
            full_filename = f"{filename}.{file_extension}"
            
            return ContentFile(response.content, name=full_filename)
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'⚠️ No se pudo descargar la imagen {url}: {str(e)}')
            )
            return None

    def handle(self, *args, **options):
        self.stdout.write('Creando tarjetas de ejemplo...')
        
        # Verificar configuración de Cloudinary
        if is_cloudinary_configured():
            self.stdout.write(self.style.SUCCESS('✅ Cloudinary configurado - Las imágenes se subirán a la nube'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Cloudinary no configurado - Las imágenes se guardarán localmente'))
        
        # Mostrar formatos soportados
        supported_formats = get_supported_formats()
        self.stdout.write(f'📸 Formatos de imagen soportados: {", ".join(supported_formats)}')
        
        cards_data = [
            {
                'title': 'Tarjeta de Débito',
                'description': 'Accede a tu dinero de forma segura y conveniente, con beneficios exclusivos en cada compra.',
                'card_type': 'debit',
                'banner_image_url': 'https://images.pexels.com/photos/6214474/pexels-photo-6214474.jpeg?auto=compress&cs=tinysrgb&w=1600',
                'card_image_url': 'https://images.pexels.com/photos/4386366/pexels-photo-4386366.jpeg?auto=compress&cs=tinysrgb&w=800',
                'benefits': [
                    {'icon': 'FaShieldAlt', 'text': 'Seguridad Avanzada - Protección contra fraudes y tecnología de chip EMV'},
                    {'icon': 'FaGlobeAmericas', 'text': 'Aceptación Global - Utiliza tu tarjeta en millones de establecimientos en todo el mundo'},
                    {'icon': 'FaMobileAlt', 'text': 'Control Móvil - Gestiona tu tarjeta y tus gastos desde nuestra app móvil'},
                ],
                'features': 'Sin cuota anual, Reembolso de cargos en cajeros automáticos, Programa de recompensas por uso, Notificaciones instantáneas de transacciones',
                'requirements': 'Ser titular de una cuenta corriente o de ahorros, Documento de identidad válido, Comprobante de domicilio reciente, Cumplir con los requisitos mínimos de saldo en cuenta'
            },
            {
                'title': 'Tarjeta de Crédito Premium',
                'description': 'Disfruta de beneficios exclusivos y recompensas premium con nuestra tarjeta de crédito de alto nivel.',
                'card_type': 'credit',
                'benefits': [
                    {'icon': 'FaGem', 'text': 'Beneficios Premium - Acceso a salas VIP en aeropuertos y hoteles de lujo'},
                    {'icon': 'FaStar', 'text': 'Recompensas Exclusivas - Puntos premium que valen más en viajes y entretenimiento'},
                    {'icon': 'FaCrown', 'text': 'Servicio Concierge - Asistencia personalizada 24/7 para todos tus viajes'},
                ],
                'features': 'Línea de crédito alta, Sin comisión anual el primer año, Seguro de viaje incluido, Protección de compras',
                'requirements': 'Ingresos mínimos de $5,000 mensuales, Historial crediticio excelente, Documentos de identidad vigentes, Comprobantes de ingresos'
            },
            {
                'title': 'Tarjeta Empresarial',
                'description': 'Herramienta financiera completa para empresas con control total sobre gastos y reportes detallados.',
                'card_type': 'business',
                'benefits': [
                    {'icon': 'FaBuilding', 'text': 'Gestión Empresarial - Control total sobre gastos de la empresa'},
                    {'icon': 'FaChartLine', 'text': 'Reportes Detallados - Análisis completo de gastos por departamento'},
                    {'icon': 'FaUsers', 'text': 'Tarjetas Adicionales - Emite tarjetas para empleados con límites personalizados'},
                ],
                'features': 'Límites de gasto personalizables, Reportes mensuales detallados, Integración con software contable, Tarjetas adicionales sin costo',
                'requirements': 'Empresa registrada legalmente, Documentos comerciales vigentes, Plan de negocio, Ingresos mínimos de $10,000 mensuales'
            }
        ]
        
        created_count = 0
        for card_item in cards_data:
            card, created = Card.objects.get_or_create(
                title=card_item['title'],
                defaults={
                    'description': card_item['description'],
                    'card_type': card_item['card_type'],
                    'features': card_item['features'],
                    'requirements': card_item['requirements'],
                    'is_active': True
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(f'✓ Tarjeta "{card_item["title"]}" creada')
                
                # Descargar y guardar imágenes si están disponibles
                if 'banner_image_url' in card_item and card_item['banner_image_url']:
                    banner_file = self.download_image(
                        card_item['banner_image_url'], 
                        f'banner_card_{card.id}'
                    )
                    if banner_file:
                        card.banner_image.save(banner_file.name, banner_file, save=True)
                        self.stdout.write(f'  ✓ Imagen de banner descargada ({banner_file.name})')
                
                if 'card_image_url' in card_item and card_item['card_image_url']:
                    card_file = self.download_image(
                        card_item['card_image_url'], 
                        f'card_{card.id}'
                    )
                    if card_file:
                        card.card_image.save(card_file.name, card_file, save=True)
                        self.stdout.write(f'  ✓ Imagen de tarjeta descargada ({card_file.name})')
                
                # Crear los beneficios para esta tarjeta
                for benefit_data in card_item['benefits']:
                    CardBenefit.objects.create(
                        card=card,
                        icon=benefit_data['icon'],
                        text=benefit_data['text']
                    )
                    self.stdout.write(f'  ✓ Beneficio "{benefit_data["icon"]}" agregado')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} tarjetas de ejemplo creadas exitosamente'
            )
        )
