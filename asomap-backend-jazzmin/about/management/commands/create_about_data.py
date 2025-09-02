from django.core.management.base import BaseCommand
from django.utils import timezone
from about.models import (
    Hero, QuienesSomos, NuestraHistoria, Mision, Vision, 
    Valor, Director
)
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Crear datos iniciales para la aplicación About'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forzar la creación aunque ya existan datos',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('📝 Creando datos iniciales de About...')
        )

        try:
            # 1. Hero Section
            if not Hero.objects.exists() or options['force']:
                hero, created = Hero.objects.get_or_create(
                    title="Asociación de Ahorros y Préstamos Moca",
                    defaults={
                        'description': "Más de 50 años sirviendo a la comunidad de Moca y sus alrededores con servicios financieros confiables y accesibles. Somos una institución sin fines de lucro comprometida con el desarrollo económico de nuestras familias.",
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write('✓ Hero section creado')
                else:
                    self.stdout.write('✓ Hero section actualizado')

            # 2. Quienes Somos
            if not QuienesSomos.objects.exists() or options['force']:
                quienes_somos, created = QuienesSomos.objects.get_or_create(
                    title="Quiénes Somos",
                                    defaults={
                    'paragraphs': "La Asociación de Ahorros y Préstamos Moca (ASOMAP) fue fundada en 1969 por un grupo de visionarios empresarios y líderes comunitarios de la ciudad de Moca, con el objetivo de promover el ahorro y facilitar el acceso al crédito para el desarrollo económico local.\n\nDesde nuestros inicios, hemos mantenido un compromiso inquebrantable con nuestros valores fundamentales: la transparencia, la confianza, la solidaridad y el servicio a la comunidad.\n\nHoy, ASOMAP es una de las instituciones financieras más respetadas de la región del Cibao, sirviendo a más de 15,000 asociados.",
                    'is_active': True
                }
                )
                if created:
                    self.stdout.write('✓ Quienes Somos creado')
                else:
                    self.stdout.write('✓ Quienes Somos actualizado')

            # 3. Nuestra Historia
            if not NuestraHistoria.objects.exists() or options['force']:
                historia, created = NuestraHistoria.objects.get_or_create(
                    title="Nuestra Historia",
                    defaults={
                        'paragraphs': "ASOMAP nació en 1969 como respuesta a la necesidad de una institución financiera que sirviera a la comunidad de Moca. Un grupo de empresarios visionarios se unió para crear una cooperativa que promoviera el ahorro y facilitara el acceso al crédito.\n\nA lo largo de más de 50 años, hemos crecido de manera sostenible, siempre manteniendo nuestros valores fundamentales y nuestro compromiso con la comunidad. Hemos sido testigos del desarrollo de Moca y hemos contribuido activamente a su progreso económico.\n\nHoy somos una institución sólida y respetada, con más de 15,000 asociados y una presencia significativa en la región del Cibao.",
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write('✓ Nuestra Historia creada')
                else:
                    self.stdout.write('✓ Nuestra Historia actualizada')

            # 4. Mision
            if not Mision.objects.exists() or options['force']:
                mision, created = Mision.objects.get_or_create(
                    title="Nuestra Misión",
                                    defaults={
                    'description': "Proveer y fomentar el ahorro sistemático entre nuestros asociados\n\nFacilitar el acceso al crédito en condiciones justas y accesibles\n\nPromover el desarrollo económico y social de la comunidad de Moca\n\nOfrecer servicios financieros de calidad con transparencia y confianza",
                    'is_active': True
                }
                )
                if created:
                    self.stdout.write('✓ Misión creada')
                else:
                    self.stdout.write('✓ Misión actualizada')

            # 5. Vision
            if not Vision.objects.exists() or options['force']:
                vision, created = Vision.objects.get_or_create(
                    title="Nuestra Visión",
                                    defaults={
                    'description': "Ser la institución financiera líder en servicios de ahorro y préstamos en la región del Cibao\n\nReconocida por nuestra excelencia en el servicio al cliente y nuestra contribución al desarrollo comunitario\n\nMantenernos a la vanguardia de la innovación tecnológica en servicios financieros",
                    'is_active': True
                }
                )
                if created:
                    self.stdout.write('✓ Visión creada')
                else:
                    self.stdout.write('✓ Visión actualizada')

            # 6. Valores
            valores_data = [
                {
                    'title': 'Transparencia',
                    'description': 'Actuamos con honestidad y claridad en todas nuestras operaciones.'
                },
                {
                    'title': 'Confianza',
                    'description': 'Construimos relaciones duraderas basadas en la confianza mutua.'
                },
                {
                    'title': 'Solidaridad',
                    'description': 'Promovemos la ayuda mutua y el apoyo entre nuestros asociados.'
                },
                {
                    'title': 'Excelencia',
                    'description': 'Buscamos la excelencia en todo lo que hacemos.'
                }
            ]

            for valor_data in valores_data:
                valor, created = Valor.objects.get_or_create(
                    title=valor_data['title'],
                    defaults={
                        'description': valor_data['description'],
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write(f'✓ Valor "{valor_data["title"]}" creado')

            # 7. Directores
            directores_data = [
                {'name': 'Dr. Juan Carlos Rodríguez', 'position': 'Presidente del Consejo'},
                {'name': 'Lic. María Elena Santos', 'position': 'Vicepresidenta'},
                {'name': 'Ing. Roberto Fernández', 'position': 'Secretario'},
                {'name': 'Lic. Ana Patricia López', 'position': 'Tesorera'},
                {'name': 'Dr. Carlos Manuel Herrera', 'position': 'Vocal'},
            ]

            for director_data in directores_data:
                director, created = Director.objects.get_or_create(
                    name=director_data['name'],
                    defaults={
                        'position': director_data['position'],
                        'is_active': True
                    }
                )
                if created:
                    self.stdout.write(f'✓ Director "{director_data["name"]}" creado')

            # 8. Community Support (comentado - se maneja en otro comando)
            self.stdout.write('ℹ️  Community Support se maneja en create_community_data')

            self.stdout.write(
                self.style.SUCCESS('�� Datos iniciales de About creados exitosamente!')
            )

        except Exception as e:
            logger.error(f'Error creando datos de About: {e}')
            self.stdout.write(
                self.style.ERROR(f'❌ Error creando datos: {e}')
            )
            raise 