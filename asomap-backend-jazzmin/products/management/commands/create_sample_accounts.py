"""
Comando de gestión para crear cuentas de ejemplo
"""
import requests
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings
from products.models import Account, AccountBenefit
from core.cloudinary_utils import is_cloudinary_configured, get_supported_formats


class Command(BaseCommand):
    help = 'Crea cuentas de ejemplo para el frontend'

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
        self.stdout.write('Creando cuentas de ejemplo...')
        
        # Verificar configuración de Cloudinary
        if is_cloudinary_configured():
            self.stdout.write(self.style.SUCCESS('✅ Cloudinary configurado - Las imágenes se subirán a la nube'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Cloudinary no configurado - Las imágenes se guardarán localmente'))
        
        # Mostrar formatos soportados
        supported_formats = get_supported_formats()
        self.stdout.write(f'📸 Formatos de imagen soportados: {", ".join(supported_formats)}')
        
        accounts_data = [
            {
                'title': 'Cuenta Física Clásica',
                'description': 'Nuestra Cuenta Física Clásica ofrece una solución bancaria tradicional con todas las comodidades modernas. Ideal para quienes prefieren una experiencia bancaria tangible con acceso a servicios digitales.',
                'category': 'classic_physical',
                'banner_image_url': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&h=400&q=80',
                'account_image_url': 'https://images.unsplash.com/photo-1601597111158-2fceff292cdc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=400&q=80',
                'benefits': [
                    {'icon': 'FaMoneyBillWave', 'text': 'Acceso a efectivo en cualquier momento a través de nuestra red de cajeros automáticos'},
                    {'icon': 'FaCreditCard', 'text': 'Tarjeta de débito para compras en establecimientos y en línea'},
                    {'icon': 'FaMobileAlt', 'text': 'Banca móvil y en línea para gestionar tu cuenta en cualquier momento'},
                ],
                'features': 'Sin comisión por mantenimiento de cuenta, Retiros gratuitos en cajeros de nuestra red, Transferencias interbancarias sin costo, Notificaciones de transacciones por SMS o correo electrónico',
                'requirements': 'Ser mayor de 18 años, Documento de identidad válido, Comprobante de domicilio reciente, Depósito inicial mínimo de $100'
            },
            {
                'title': 'Cuenta de Ahorros Premium',
                'description': 'Diseñada para maximizar tus ahorros con tasas de interés competitivas y beneficios exclusivos para clientes premium.',
                'category': 'savings',
                'benefits': [
                    {'icon': 'FaChartLine', 'text': 'Tasa de interés alta hasta 5% anual en saldos superiores a $10,000'},
                    {'icon': 'FaShieldAlt', 'text': 'Sin comisiones por mantenimiento o transacciones'},
                    {'icon': 'FaGift', 'text': 'Acceso prioritario a nuevos productos y servicios'},
                ],
                'features': 'Tasa de interés competitiva, Sin comisiones por mantenimiento, Acceso a banca en línea, Transferencias gratuitas',
                'requirements': 'Ser mayor de 18 años, Documento de identidad válido, Depósito inicial mínimo de $500, Ingresos mínimos de $2,000 mensuales'
            },
            {
                'title': 'Cuenta Empresarial',
                'description': 'Solución bancaria completa para empresas con herramientas de gestión financiera avanzadas.',
                'category': 'business',
                'benefits': [
                    {'icon': 'FaHandshake', 'text': 'Gestión de nómina automatizada y sin comisiones'},
                    {'icon': 'FaChartLine', 'text': 'Reportes financieros detallados y personalizables'},
                    {'icon': 'FaUserShield', 'text': 'Acceso múltiple para diferentes usuarios de la empresa'},
                ],
                'features': 'Gestión de nómina automatizada, Reportes financieros detallados, Acceso múltiple para usuarios, Línea de crédito empresarial',
                'requirements': 'Empresa registrada legalmente, Documentos comerciales vigentes, Plan de negocio, Depósito inicial mínimo de $1,000'
            }
        ]
        
        created_count = 0
        for account_item in accounts_data:
            account, created = Account.objects.get_or_create(
                title=account_item['title'],
                defaults={
                    'description': account_item['description'],
                    'category': account_item['category'],
                    'features': account_item['features'],
                    'requirements': account_item['requirements'],
                    'is_active': True
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(f'✓ Cuenta "{account_item["title"]}" creada')
                
                # Descargar y guardar imágenes si están disponibles
                if 'banner_image_url' in account_item and account_item['banner_image_url']:
                    banner_file = self.download_image(
                        account_item['banner_image_url'], 
                        f'banner_{account.id}'
                    )
                    if banner_file:
                        account.banner_image.save(banner_file.name, banner_file, save=True)
                        self.stdout.write(f'  ✓ Imagen de banner descargada ({banner_file.name})')
                
                if 'account_image_url' in account_item and account_item['account_image_url']:
                    account_file = self.download_image(
                        account_item['account_image_url'], 
                        f'account_{account.id}'
                    )
                    if account_file:
                        account.account_image.save(account_file.name, account_file, save=True)
                        self.stdout.write(f'  ✓ Imagen de cuenta descargada ({account_file.name})')
                
                # Crear los beneficios para esta cuenta
                for benefit_data in account_item['benefits']:
                    AccountBenefit.objects.create(
                        account=account,
                        icon=benefit_data['icon'],
                        text=benefit_data['text']
                    )
                    self.stdout.write(f'  ✓ Beneficio "{benefit_data["icon"]}" agregado')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} cuentas de ejemplo creadas exitosamente'
            )
        )
