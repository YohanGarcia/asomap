"""
Comando de gestión para crear certificados de ejemplo
"""
import requests
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings
from products.models import (
    Certificate, CertificateBenefit, CertificateRate, 
    CertificateDepositRate, CertificateFAQ
)
from core.cloudinary_utils import is_cloudinary_configured, get_supported_formats


class Command(BaseCommand):
    help = 'Crea certificados de ejemplo para el frontend'

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
        self.stdout.write('Creando certificados de ejemplo...')
        
        # Verificar configuración de Cloudinary
        if is_cloudinary_configured():
            self.stdout.write(self.style.SUCCESS('✅ Cloudinary configurado - Las imágenes se subirán a la nube'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Cloudinary no configurado - Las imágenes se guardarán localmente'))
        
        # Mostrar formatos soportados
        supported_formats = get_supported_formats()
        self.stdout.write(f'📸 Formatos de imagen soportados: {", ".join(supported_formats)}')
        
        certificates_data = [
            {
                'title': 'Certificado Financiero',
                'subtitle': 'Multiplica tu dinero con un depósito a plazo fijo',
                'description': 'Invierte tu dinero de forma segura y obtén los mejores rendimientos del mercado con nuestro certificado financiero.',
                'certificate_type': 'financial',
                'banner_image_url': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&h=400&q=80',
                'certificate_image_url': 'https://images.unsplash.com/photo-1601597111158-2fceff292cdc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=400&q=80',
                'cta_apply': 'Solicitar',
                'cta_rates': 'Tarifario',
                'benefits_title': 'Beneficios de tu Certificado Financiero',
                'investment_title': 'Tu nueva Inversión',
                'investment_subtitle': 'Especificaciones del depósito a plazo fijo para personas:',
                'investment_details': [
                    'Plazo desde 30 a 180 días',
                    'Requiere de una apertura de cuenta de ahorro o corriente',
                    'Inversión desde $5,000,000.00',
                    'Pago de interés al vencimiento de tu inversión',
                    'Acerca tasa de interés según plazo y el monto de apertura',
                    'Acceso en todo momento a la información desde tu Internet Banking'
                ],
                'rates_title': 'Tarifas',
                'requirements_title': 'Requisitos',
                'requirements': [
                    'El menor debe hacerse acompañar de uno de sus padres o tutor',
                    'Identificación oficial vigente del representante o tutor',
                    'Acta de nacimiento original del menor de edad'
                ],
                'deposit_rates_title': 'Escala de Tasas de Captaciones de Depósitos',
                'deposit_rates_valid_from': 'Vigente desde el 31 de enero del 2023',
                'faq_title': 'Preguntas Frecuentes Certificado Financiero',
                'benefits': [
                    {'title': 'Alta rentabilidad', 'description': 'Obtén los mejores rendimientos del mercado'},
                    {'title': 'Flexibilidad', 'description': 'Elige el plazo que más te convenga'},
                    {'title': 'Confianza', 'description': 'Respaldado por una institución sólida'},
                    {'title': 'Manejo en línea', 'description': 'Gestiona tu inversión desde cualquier lugar'},
                ],
                'rates': [
                    {'label': 'Monto de apertura', 'value': '$5,000,000.00'},
                    {'label': 'Balance mínimo para el cobro de la comisión', 'value': '$5,000,000.00'},
                    {'label': 'Pago de interés Anual', 'value': '9.5%'},
                    {'label': 'Comisión por débajo de balance mínimo', 'value': '$500.00'},
                    {'label': 'Comisión por cancelación antes de un mes transcurrido', 'value': 'Exonerada'},
                    {'label': 'Reposición por libreta perdida', 'value': '$250.00'},
                ],
                'deposit_rates': [
                    {'range': 'De 10,000.00 a 500,000.00', 'rate': '5%', 'term': 'de 30 a 90 días'},
                    {'range': 'De 500,001.00 a 1,000,000.00', 'rate': '6%', 'term': 'de 30 a 90 días'},
                    {'range': 'De 1,000,001.00 a 3,000,000.00', 'rate': '7.5%', 'term': 'de 30 a 90 días'},
                    {'range': '3,000,001.00 EN ADELANTE', 'rate': '8%', 'term': 'De 30 a 90 días'},
                ],
                'faqs': [
                    {
                        'question': '¿Qué es una inversión?',
                        'answer': 'Una inversión es la colocación de capital en una operación, proyecto o iniciativa empresarial con el fin de obtener una ganancia en el futuro.'
                    },
                    {
                        'question': '¿Cuáles son los requisitos para abrir una inversión en ASOMAP?',
                        'answer': 'Los requisitos específicos pueden variar. Por favor, consulte con un representante de ASOMAP para obtener la información más actualizada.'
                    },
                    {
                        'question': '¿Cuáles son los plazos disponibles para mi inversión?',
                        'answer': 'Los plazos disponibles van desde 30 hasta 180 días, según lo mencionado en las especificaciones de la inversión.'
                    }
                ]
            }
        ]
        
        created_count = 0
        for cert_item in certificates_data:
            certificate, created = Certificate.objects.get_or_create(
                title=cert_item['title'],
                defaults={
                    'subtitle': cert_item['subtitle'],
                    'description': cert_item['description'],
                    'certificate_type': cert_item['certificate_type'],
                    'cta_apply': cert_item['cta_apply'],
                    'cta_rates': cert_item['cta_rates'],
                    'benefits_title': cert_item['benefits_title'],
                    'investment_title': cert_item['investment_title'],
                    'investment_subtitle': cert_item['investment_subtitle'],
                    'investment_details': ', '.join(cert_item['investment_details']),
                    'rates_title': cert_item['rates_title'],
                    'requirements_title': cert_item['requirements_title'],
                    'requirements': ', '.join(cert_item['requirements']),
                    'deposit_rates_title': cert_item['deposit_rates_title'],
                    'deposit_rates_valid_from': cert_item['deposit_rates_valid_from'],
                    'faq_title': cert_item['faq_title'],
                    'is_active': True
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(f'✓ Certificado "{cert_item["title"]}" creado')
                
                # Descargar y guardar imagen de banner
                if 'banner_image_url' in cert_item:
                    banner_image = self.download_image(cert_item['banner_image_url'], f'banner_certificate_{certificate.id}')
                    if banner_image:
                        certificate.banner_image.save(f'banner_certificate_{certificate.id}.jpg', banner_image, save=True)
                        self.stdout.write(f'  ✓ Imagen de banner descargada (banner_certificate_{certificate.id}.jpg)')
                
                # Descargar y guardar imagen del certificado
                if 'certificate_image_url' in cert_item:
                    certificate_image = self.download_image(cert_item['certificate_image_url'], f'certificate_{certificate.id}')
                    if certificate_image:
                        certificate.certificate_image.save(f'certificate_{certificate.id}.jpg', certificate_image, save=True)
                        self.stdout.write(f'  ✓ Imagen del certificado descargada (certificate_{certificate.id}.jpg)')
                
                # Crear los beneficios para este certificado
                for benefit_data in cert_item['benefits']:
                    CertificateBenefit.objects.create(
                        certificate=certificate,
                        title=benefit_data['title'],
                        description=benefit_data['description']
                    )
                    self.stdout.write(f'  ✓ Beneficio "{benefit_data["title"]}" agregado')
                
                # Crear las tarifas para este certificado
                for rate_data in cert_item['rates']:
                    CertificateRate.objects.create(
                        certificate=certificate,
                        label=rate_data['label'],
                        value=rate_data['value']
                    )
                    self.stdout.write(f'  ✓ Tarifa "{rate_data["label"]}" agregada')
                
                # Crear las tasas de depósito para este certificado
                for deposit_rate_data in cert_item['deposit_rates']:
                    CertificateDepositRate.objects.create(
                        certificate=certificate,
                        range=deposit_rate_data['range'],
                        rate=deposit_rate_data['rate'],
                        term=deposit_rate_data['term']
                    )
                    self.stdout.write(f'  ✓ Tasa de depósito "{deposit_rate_data["range"]}" agregada')
                
                # Crear las preguntas frecuentes para este certificado
                for faq_data in cert_item['faqs']:
                    CertificateFAQ.objects.create(
                        certificate=certificate,
                        question=faq_data['question'],
                        answer=faq_data['answer']
                    )
                    self.stdout.write(f'  ✓ FAQ "{faq_data["question"][:30]}..." agregada')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} certificados de ejemplo creados exitosamente'
            )
        )
