"""
Comando de gestión para crear datos de ejemplo de la página de inicio
"""
from django.core.management.base import BaseCommand
from home.models import (
    DebitCardPromo, EducationItem, EducationSection, 
    PeKeAccountSummary, Product, ProductSection, SliderItem
)


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para la página de inicio'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo para la página de inicio...')
        
        try:
            # Crear promoción de tarjeta de débito
            promo = DebitCardPromo.objects.get_or_create(
                defaults={
                    'title': "Obtén tu tarjeta de débito",
                    'highlighted_title': "ASOMAP",
                    'description': "Disfruta de todos los beneficios de nuestra tarjeta de débito. Sin comisiones ocultas, acceso a cajeros automáticos en todo el país y la seguridad de ASOMAP respaldando cada transacción.",
                    'primary_button_text': "Solicitar tarjeta",
                    'secondary_button_text': "Conocer beneficios",
                    'image_alt': "Tarjeta de débito ASOMAP con diseño moderno",
                    'is_active': True
                }
            )[0]
            
            # Crear elementos educativos
            education_items_data = [
                {
                    'alt': 'Taller de finanzas personales',
                    'description': 'Aprende a manejar tu dinero de manera inteligente con nuestros talleres de finanzas personales.',
                    'order': 1
                },
                {
                    'alt': 'Seminario de inversiones',
                    'description': 'Descubre las mejores estrategias de inversión con expertos financieros.',
                    'order': 2
                },
                {
                    'alt': 'Curso de ahorro',
                    'description': 'Técnicas efectivas para ahorrar y alcanzar tus metas financieras.',
                    'order': 3
                },
                {
                    'alt': 'Workshop de presupuesto',
                    'description': 'Aprende a crear y mantener un presupuesto efectivo para tu hogar.',
                    'order': 4
                }
            ]
            
            education_items = []
            for item_data in education_items_data:
                item = EducationItem.objects.get_or_create(
                    alt=item_data['alt'],
                    defaults={
                        'description': item_data['description'],
                        'order': item_data['order'],
                        'is_active': True
                    }
                )[0]
                education_items.append(item)
            
            # Crear sección de educación
            education_section = EducationSection.objects.get_or_create(
                defaults={
                    'title': 'Educación Financiera',
                    'subtitle': 'Empodérate con conocimiento financiero',
                    'footer_text': 'Únete a nuestros programas educativos y toma el control de tu futuro financiero.',
                    'is_active': True
                }
            )[0]
            
            # Asociar elementos con la sección
            education_section.education_items.set(education_items)
            
            # Crear productos basados en productData.ts
            products_data = [
                {
                    'title': '¡Tus sueños, tu Préstamo!',
                    'description': 'Obtenlo en menos 30 minutos a través de nuestros canales digitales.',
                    'category': 'prestamos',
                    'image_width': 600,
                    'image_height': 400,
                    'order': 1
                },
                {
                    'title': 'Cuenta de Ahorros',
                    'description': 'Abre tu cuenta y empieza a ahorrar hoy mismo.',
                    'category': 'cuentas',
                    'image_width': 600,
                    'image_height': 400,
                    'order': 2
                },
                {
                    'title': 'Tarjeta de Debito',
                    'description': 'Abre tu cuenta y empieza a utilizar para tus compras y retiros.',
                    'category': 'tarjetas',
                    'image_width': 600,
                    'image_height': 400,
                    'order': 3
                }
            ]
            
            created_products = []
            for product_data in products_data:
                product = Product.objects.get_or_create(
                    title=product_data['title'],
                    defaults={
                        'description': product_data['description'],
                        'category': product_data['category'],
                        'image_width': product_data['image_width'],
                        'image_height': product_data['image_height'],
                        'order': product_data['order'],
                        'is_active': True
                    }
                )[0]
                created_products.append(product)
                self.stdout.write(f'✓ Producto "{product_data["title"]}" creado')
            
            # Crear sección de productos
            product_section = ProductSection.objects.get_or_create(
                defaults={
                    'title': '¿Qué necesitas hoy?',
                    'subtitle': '¡Mira los productos que tenemos para ti online!',
                    'button_text': '¡Solicítalo!',
                    'is_active': True
                }
            )[0]
            
            # Asociar productos con la sección
            product_section.products.set(created_products)
            
            # Crear resumen de cuenta PeKe basado en pekeAccountSummaryData.ts
            peke_account = PeKeAccountSummary.objects.get_or_create(
                defaults={
                    'title': 'Haz tu aporte y juntos apoyemos a los niños con la cuenta Pekes',
                    'description': 'Recolecta monedas, sube tu puntaje y participa por increíbles premios',
                    'button_text': '¡Solicítalo!',
                    'image_alt': 'Niño y adulto en bicicleta',
                    'is_active': True
                }
            )[0]
            
            self.stdout.write(f'✓ Resumen de cuenta PeKe creado: {peke_account.title}')
            
            # Crear elementos del slider basados en sliderData.ts
            slider_items_data = [
                {
                    'alt': 'Asomap Banking',
                    'order': 1
                },
                {
                    'alt': 'Créditos Comerciales',
                    'order': 2
                },
                {
                    'alt': 'Créditos Microcrédito',
                    'order': 3
                },
                {
                    'alt': 'Cuentas Pekes',
                    'order': 4
                },
                {
                    'alt': 'Préstamo Personal',
                    'order': 5
                },
                {
                    'alt': 'Prousuario',
                    'order': 6
                }
            ]
            
            created_slider_items = []
            for slider_data in slider_items_data:
                slider_item = SliderItem.objects.get_or_create(
                    alt=slider_data['alt'],
                    defaults={
                        'order': slider_data['order'],
                        'is_active': True
                    }
                )[0]
                created_slider_items.append(slider_item)
                self.stdout.write(f'✓ Slider item "{slider_data["alt"]}" creado')
            
            self.stdout.write(
                self.style.SUCCESS(
                    '✅ Datos de la página de inicio creados exitosamente:\n'
                    f'  - 1 promoción de tarjeta de débito\n'
                    f'  - Título: {promo.title}\n'
                    f'  - Título destacado: {promo.highlighted_title}\n'
                    f'  - Estado: {"Activo" if promo.is_active else "Inactivo"}\n'
                    f'  - 1 sección de educación\n'
                    f'  - {len(education_items)} elementos educativos\n'
                    f'  - 1 sección de productos\n'
                    f'  - {len(created_products)} productos\n'
                    f'  - 1 resumen de cuenta PeKe\n'
                    f'  - {len(created_slider_items)} elementos del slider'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear datos de la página de inicio: {e}')
            )
