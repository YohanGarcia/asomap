from django.core.management.base import BaseCommand
from about.models import CommunityCategory, CommunityInitiative, CommunitySupport, COMMUNITY_CATEGORIES_DATA, COMMUNITY_INITIATIVES_DATA

class Command(BaseCommand):
    help = 'Crea datos iniciales básicos para las categorías e iniciativas de apoyo comunitario (sin imágenes)'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos iniciales básicos de apoyo comunitario...')
        
        # Crear o actualizar CommunitySupport principal
        try:
            community_support, created = CommunitySupport.objects.get_or_create(
                id=1,
                defaults={
                    'title': 'Apoyo a la Comunidad',
                    'description': 'Dentro de nuestra política de responsabilidad social, la Asociación Mocana de Ahorros y Préstamos contribuye con las instituciones sin fines de lucro que trabajan a favor de los más necesitados en la zona de incidencia de la entidad. Asimismo, aporta a las entidades propulsoras del deporte y la cultura de la región.',
                    'is_active': True
                }
            )
            
            if created:
                self.stdout.write(f'  ✓ CommunitySupport creado: {community_support.title}')
            else:
                # Actualizar la descripción si ya existe
                community_support.description = 'Dentro de nuestra política de responsabilidad social, la Asociación Mocana de Ahorros y Préstamos contribuye con las instituciones sin fines de lucro que trabajan a favor de los más necesitados en la zona de incidencia de la entidad. Asimismo, aporta a las entidades propulsoras del deporte y la cultura de la región.'
                community_support.save()
                self.stdout.write(f'  ✓ CommunitySupport actualizado: {community_support.title}')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'  ✗ Error con CommunitySupport: {e}')
            )
        
        # Crear categorías
        categories_created = 0
        for category_data in COMMUNITY_CATEGORIES_DATA:
            try:
                category, created = CommunityCategory.objects.get_or_create(
                    name=category_data['name'],
                    defaults={
                        'icon': category_data['icon'],
                        'description': category_data['description'],
                        'is_active': True
                    }
                )
                if created:
                    categories_created += 1
                    self.stdout.write(f'  ✓ Categoría creada: {category.name}')
                else:
                    self.stdout.write(f'  - Categoría ya existe: {category.name}')
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'  ✗ Error con categoría {category_data["name"]}: {e}')
                )
        
        # Crear iniciativas (sin imágenes)
        initiatives_created = 0
        for initiative_data in COMMUNITY_INITIATIVES_DATA:
            try:
                category = CommunityCategory.objects.get(name=initiative_data['category_name'])
                initiative, created = CommunityInitiative.objects.get_or_create(
                    title=initiative_data['title'],
                    defaults={
                        'description': initiative_data['description'],
                        'impact': initiative_data['impact'],
                        'category': category,
                        'is_active': True
                    }
                )
                if created:
                    initiatives_created += 1
                    self.stdout.write(f'  ✓ Iniciativa creada: {initiative.title}')
                else:
                    self.stdout.write(f'  - Iniciativa ya existe: {initiative.title}')
            except CommunityCategory.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'  ✗ Categoría no encontrada: {initiative_data["category_name"]}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'  ✗ Error con iniciativa {initiative_data["title"]}: {e}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Datos básicos creados exitosamente:\n'
                f'  - CommunitySupport: {"creado" if created else "actualizado"}\n'
                f'  - Categorías: {categories_created} nuevas\n'
                f'  - Iniciativas: {initiatives_created} nuevas\n\n'
                f'💡 Nota: Las imágenes se pueden agregar manualmente desde el admin de Django.'
            )
        )
