"""
Comando de gestión para crear datos de ejemplo de educación financiera
"""
import requests
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings
from educacionfinanciera.models import SavingTip, SliderSlide, FAQItem
from core.cloudinary_utils import is_cloudinary_configured, get_supported_formats


class Command(BaseCommand):
    help = 'Crea datos de ejemplo de educación financiera para el frontend'

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
        self.stdout.write('Creando datos de ejemplo de educación financiera...')
        
        # Verificar configuración de Cloudinary
        if is_cloudinary_configured():
            self.stdout.write(self.style.SUCCESS('✅ Cloudinary configurado - Las imágenes se subirán a la nube'))
        else:
            self.stdout.write(self.style.WARNING('⚠️ Cloudinary no configurado - Las imágenes se guardarán localmente'))
        
        # Mostrar formatos soportados
        supported_formats = get_supported_formats()
        self.stdout.write(f'📸 Formatos de imagen soportados: {", ".join(supported_formats)}')
        
        # Datos de consejos de ahorro
        saving_tips_data = [
            {
                'title': '¿Qué es la educación financiera?',
                'description': 'Usar el dinero eficientemente para evitar problemas de solvencia.',
                'content': '<p>La <strong>educación financiera</strong> es el proceso de aprender a manejar el dinero de manera efectiva. Incluye aprender sobre:</p><ul><li><strong>Presupuestos:</strong> Planificar tus gastos e ingresos</li><li><strong>Ahorro:</strong> Guardar dinero para el futuro</li><li><strong>Inversión:</strong> Hacer crecer tu dinero</li><li><strong>Crédito:</strong> Manejar préstamos responsablemente</li><li><strong>Gestión de deudas:</strong> Pagar lo que debes a tiempo</li></ul><p>Es fundamental para tomar decisiones financieras informadas y alcanzar la estabilidad económica.</p>',
                'link': 'https://www.educacionfinanciera.org',
                'image_url': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&h=400&q=80',
                'order': 1
            },
            {
                'title': 'Hábitos Financieros',
                'description': 'Ahorra regularmente y prioriza tus necesidades.',
                'content': '<p>Desarrollar <strong>buenos hábitos financieros</strong> es clave para el éxito económico a largo plazo. Algunos hábitos importantes incluyen:</p><ul><li><strong>Establecer un presupuesto mensual:</strong> Planifica tus gastos e ingresos</li><li><strong>Vivir por debajo de tus posibilidades:</strong> No gastes más de lo que ganas</li><li><strong>Ahorrar automáticamente:</strong> Guarda una parte de tus ingresos</li><li><strong>Evitar deudas innecesarias:</strong> Solo pide préstamos cuando sea realmente necesario</li></ul><p>Recuerda: los hábitos se construyen con tiempo y consistencia.</p>',
                'link': 'https://www.example.com/habitos-financieros',
                'image_url': 'https://images.unsplash.com/photo-1601597111158-2fceff292cdc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=400&q=80',
                'order': 2
            }
        ]
        
        # Datos de slides del slider
        slider_slides_data = [
            {
                'image_url': 'https://www.asomap.com.do/wp-content/uploads/2019/08/slider_02.png',
                'title': 'Consejos de Ahorro',
                'description': 'Mejora tus finanzas personales',
                'order': 1
            },
            {
                'image_url': 'https://www.asomap.com.do/wp-content/uploads/2019/08/slider_06.png',
                'title': 'Educación Financiera',
                'description': 'Aprende a manejar tu dinero',
                'order': 2
            },
            {
                'image_url': 'https://www.asomap.com.do/wp-content/uploads/2024/01/Consejos-de-Ciberseguridad-Ai-02.png',
                'title': 'Ciberseguridad',
                'description': 'Protege tu información financiera',
                'order': 3
            }
        ]
        
        # Datos de preguntas frecuentes
        faq_items_data = [
            {
                'question': '¿Qué es la educación financiera?',
                'answer': 'Es el conocimiento necesario para entender cómo funciona el dinero en el mundo: cómo obtenerlo, manejarlo, invertirlo y donarlo.',
                'order': 1
            },
            {
                'question': '¿Por qué es importante ahorrar?',
                'answer': 'Ahorrar te permite estar preparado para imprevistos y alcanzar tus metas financieras.',
                'order': 2
            },
            {
                'question': '¿Qué es un fondo de emergencia?',
                'answer': 'Es un ahorro destinado a cubrir gastos inesperados, como reparaciones o emergencias médicas.',
                'order': 3
            },
            {
                'question': '¿Cuánto debo ahorrar?',
                'answer': 'Un buen objetivo es ahorrar al menos el 20% de tus ingresos mensuales.',
                'order': 4
            },
            {
                'question': '¿Qué es invertir?',
                'answer': 'Invertir es usar tu dinero para comprar activos que generen un retorno, como acciones o bienes raíces.',
                'order': 5
            }
        ]
        
        # Crear consejos de ahorro
        created_tips = 0
        for tip_data in saving_tips_data:
            tip, created = SavingTip.objects.get_or_create(
                title=tip_data['title'],
                defaults={
                    'description': tip_data['description'],
                    'content': tip_data['content'],
                    'link': tip_data['link'],
                    'order': tip_data['order'],
                    'is_active': True
                }
            )
            
            if created:
                created_tips += 1
                self.stdout.write(f'✓ Consejo "{tip_data["title"]}" creado')
                
                # Descargar y guardar imagen
                if 'image_url' in tip_data:
                    image = self.download_image(tip_data['image_url'], f'tip_{tip.id}')
                    if image:
                        tip.image.save(f'tip_{tip.id}.jpg', image, save=True)
                        self.stdout.write(f'  ✓ Imagen descargada (tip_{tip.id}.jpg)')
        
        # Crear slides del slider
        created_slides = 0
        for slide_data in slider_slides_data:
            slide, created = SliderSlide.objects.get_or_create(
                title=slide_data['title'],
                defaults={
                    'description': slide_data['description'],
                    'order': slide_data['order'],
                    'is_active': True
                }
            )
            
            if created:
                created_slides += 1
                self.stdout.write(f'✓ Slide "{slide_data["title"]}" creado')
                
                # Descargar y guardar imagen
                if 'image_url' in slide_data:
                    image = self.download_image(slide_data['image_url'], f'slide_{slide.id}')
                    if image:
                        slide.image.save(f'slide_{slide.id}.jpg', image, save=True)
                        self.stdout.write(f'  ✓ Imagen descargada (slide_{slide.id}.jpg)')
        
        # Crear preguntas frecuentes
        created_faqs = 0
        for faq_data in faq_items_data:
            faq, created = FAQItem.objects.get_or_create(
                question=faq_data['question'],
                defaults={
                    'answer': faq_data['answer'],
                    'order': faq_data['order'],
                    'is_active': True
                }
            )
            
            if created:
                created_faqs += 1
                self.stdout.write(f'✓ FAQ "{faq_data["question"][:30]}..." creada')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Datos de educación financiera creados exitosamente:\n'
                f'  • {created_tips} consejos de ahorro\n'
                f'  • {created_slides} slides del slider\n'
                f'  • {created_faqs} preguntas frecuentes'
            )
        )
