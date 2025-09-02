from django.core.management.base import BaseCommand
from prousuario.models import RightsAndDutiesPage, RightsAndDutiesSection, RightsAndDutiesImage


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para Rights and Duties'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo para Rights and Duties...')
        
        # Crear página principal
        page, created = RightsAndDutiesPage.objects.get_or_create(
            page_title="Derechos y Deberes",
            defaults={
                'page_description': "En ASOMAP, nos comprometemos a mantener una relación transparente y justa con nuestros usuarios. Conocer sus derechos y deberes es fundamental para garantizar una experiencia financiera satisfactoria y segura.",
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Página creada: {page.page_title}')
        else:
            self.stdout.write(f'📄 Página existente: {page.page_title}')
        
        # Crear sección "Derechos y Deberes"
        section1, created = RightsAndDutiesSection.objects.get_or_create(
            section_id='rightsAndDuties',
            defaults={
                'title': 'Derechos y Deberes',
                'description': 'Como usuario de ASOMAP, es importante conocer tanto sus derechos fundamentales que protegen sus intereses, como sus deberes que ayudan a mantener una relación financiera saludable y beneficiosa para todos.',
                'button_text': 'Ver Derechos y Deberes',
                'additional_info': '',
                'order': 1,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Sección creada: {section1.title}')
        else:
            self.stdout.write(f'📋 Sección existente: {section1.title}')
        
        # Crear sección "Otros Derechos"
        section2, created = RightsAndDutiesSection.objects.get_or_create(
            section_id='otherRights',
            defaults={
                'title': 'Otros Derechos',
                'description': 'Además de los derechos y deberes básicos, como usuario de servicios financieros usted cuenta con derechos adicionales que complementan y fortalecen su protección como usuario de ASOMAP.',
                'button_text': 'Ver Otros Derechos',
                'additional_info': '',
                'order': 2,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Sección creada: {section2.title}')
        else:
            self.stdout.write(f'📋 Sección existente: {section2.title}')
        
        # Crear imágenes para la primera sección
        image1_1, created = RightsAndDutiesImage.objects.get_or_create(
            section=section1,
            alt_text="Derechos y Deberes 1",
            defaults={
                'description': 'Derechos y deberes fundamentales',
                'order': 1,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Imagen creada: {image1_1.alt_text}')
        else:
            self.stdout.write(f'🖼️ Imagen existente: {image1_1.alt_text}')
        
        image1_2, created = RightsAndDutiesImage.objects.get_or_create(
            section=section1,
            alt_text="Derechos y Deberes 2",
            defaults={
                'description': 'Responsabilidades y beneficios',
                'order': 2,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Imagen creada: {image1_2.alt_text}')
        else:
            self.stdout.write(f'🖼️ Imagen existente: {image1_2.alt_text}')
        
        # Crear imágenes para la segunda sección
        image2_1, created = RightsAndDutiesImage.objects.get_or_create(
            section=section2,
            alt_text="Otros Derechos 1",
            defaults={
                'description': 'Derechos complementarios',
                'order': 1,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Imagen creada: {image2_1.alt_text}')
        else:
            self.stdout.write(f'🖼️ Imagen existente: {image2_1.alt_text}')
        
        image2_2, created = RightsAndDutiesImage.objects.get_or_create(
            section=section2,
            alt_text="Otros Derechos 2",
            defaults={
                'description': 'Derechos adicionales',
                'order': 2,
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✅ Imagen creada: {image2_2.alt_text}')
        else:
            self.stdout.write(f'🖼️ Imagen existente: {image2_2.alt_text}')
        
        self.stdout.write(
            self.style.SUCCESS(
                '✅ Datos de ejemplo para Rights and Duties creados exitosamente!\n'
                '📝 Nota: Las imágenes necesitan ser subidas manualmente desde el admin.'
            )
        )
