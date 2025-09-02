"""
Comando de gestión para crear datos de ejemplo de educación financiera
"""
import requests
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings
from educacionfinanciera.models import SavingTip, SliderSlide, FAQItem


class Command(BaseCommand):
    help = 'Crea datos de ejemplo de educación financiera para el frontend'

    def download_image(self, url, filename):
        """Descarga una imagen desde una URL y la guarda en el modelo"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Extraer la extensión del archivo de la URL
            file_extension = url.split('.')[-1].split('?')[0]
            # Verificar si es un formato válido
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'webp']
            if file_extension.lower() not in valid_extensions:
                file_extension = 'jpg'  # Default a jpg si no se puede determinar
            
            full_filename = f"{filename}.{file_extension}"
            
            return ContentFile(response.content, name=full_filename)
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'⚠️ No se pudo descargar la imagen {url}: {str(e)}')
            )
            return None

    def handle(self, *args, **options):
        self.stdout.write('📚 Creando datos de ejemplo de educación financiera...')
        
        # Datos de consejos de ahorro
        saving_tips_data = [
            {
                'title': '¿Qué es la educación financiera?',
                'description': 'Usar el dinero eficientemente para evitar problemas de solvencia.',
                'content': '<p>La <strong>educación financiera</strong> es el proceso de aprender a manejar el dinero de manera efectiva. Incluye aprender sobre:</p><ul><li><strong>Presupuestos:</strong> Planificar tus gastos e ingresos</li><li><strong>Ahorro:</strong> Guardar dinero para el futuro</li><li><strong>Inversión:</strong> Hacer crecer tu dinero</li><li><strong>Crédito:</strong> Manejar préstamos responsablemente</li><li><strong>Gestión de deudas:</strong> Pagar lo que debes a tiempo</li></ul><p>Es fundamental para tomar decisiones financieras informadas y alcanzar la estabilidad económica.</p>',
                'link': 'https://www.educacionfinanciera.org',
                'order': 1
            },
            {
                'title': 'Hábitos Financieros',
                'description': 'Ahorra regularmente y prioriza tus necesidades.',
                'content': '<p>Desarrollar <strong>buenos hábitos financieros</strong> es clave para el éxito económico a largo plazo. Algunos hábitos importantes incluyen:</p><ul><li><strong>Establecer un presupuesto mensual:</strong> Planifica tus gastos e ingresos</li><li><strong>Vivir por debajo de tus posibilidades:</strong> No gastes más de lo que ganas</li><li><strong>Ahorrar automáticamente:</strong> Guarda una parte de tus ingresos</li><li><strong>Evitar deudas innecesarias:</strong> Solo pide préstamos cuando sea realmente necesario</li></ul><p>Recuerda: los hábitos se construyen con tiempo y consistencia.</p>',
                'link': 'https://www.example.com/habitos-financieros',
                'order': 2
            },
            {
                'title': 'Planificación Financiera',
                'description': 'Establece metas claras y crea un plan para alcanzarlas.',
                'content': '<p>La <strong>planificación financiera</strong> es esencial para alcanzar tus objetivos económicos. Incluye:</p><ul><li><strong>Definir metas:</strong> ¿Qué quieres lograr financieramente?</li><li><strong>Crear un presupuesto:</strong> Planifica tus ingresos y gastos</li><li><strong>Construir un fondo de emergencia:</strong> Ahorra para imprevistos</li><li><strong>Invertir para el futuro:</strong> Planifica tu retiro</li></ul><p>Un buen plan financiero te da control sobre tu dinero y te ayuda a alcanzar tus sueños.</p>',
                'link': 'https://www.example.com/planificacion-financiera',
                'order': 3
            }
        ]
        
        # Datos de slides del slider
        slider_slides_data = [
            {
                'image_url': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&h=400&q=80',
                'title': 'Consejos de Ahorro',
                'description': 'Mejora tus finanzas personales',
                'order': 1
            },
            {
                'image_url': 'https://images.unsplash.com/photo-1601597111158-2fceff292cdc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=400&q=80',
                'title': 'Educación Financiera',
                'description': 'Aprende a manejar tu dinero',
                'order': 2
            },
            {
                'image_url': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=600&h=400&q=80',
                'title': 'Planificación Financiera',
                'description': 'Construye tu futuro financiero',
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
            },
            {
                'question': '¿Cómo crear un presupuesto?',
                'answer': 'Un presupuesto es un plan que te ayuda a controlar tus gastos. Incluye todos tus ingresos y categoriza tus gastos.',
                'order': 6
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
