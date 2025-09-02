from django.core.management.base import BaseCommand
from about.models import CommunityCategory, CommunityInitiative, CommunitySupport, COMMUNITY_CATEGORIES_DATA, COMMUNITY_INITIATIVES_DATA

class Command(BaseCommand):
    help = 'Crea datos iniciales para las categorías e iniciativas de apoyo comunitario'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos iniciales de apoyo comunitario...')
        
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
        
        # Datos de iniciativas con URLs de Cloudinary
        initiatives_with_images = [
            {
                "title": "Apoyo a Instituciones Sociales",
                "description": "Contribuciones a organizaciones como el Albergue Educativo Infantil, parroquias, Centro Juvenil Don Bosco, Hogar Escuela La Milagrosa, y más.",
                "impact": "Beneficiando a múltiples instituciones en Moca, Gaspar Hernández, Cayetano Germosén, Villa Tapia y otras localidades.",
                "category_name": "Responsabilidad Social",
                "image_src": "https://res.cloudinary.com/dwqkbu2e5/image/upload/v1/media/community/initiatives/social-support.jpg",
                "image_alt": "Instituciones sociales"
            },
            {
                "title": "Iniciativas Culturales",
                "description": "Patrocinio de publicaciones, libros, brochures, conciertos populares, fiestas de carnaval, fiestas patronales y ferias multiservicios.",
                "impact": "Fortalecimiento de la identidad cultural y las tradiciones locales.",
                "category_name": "Cultura",
                "image_src": "https://res.cloudinary.com/dwqkbu2e5/image/upload/v1/media/community/initiatives/cultural-initiatives.jpg",
                "image_alt": "Iniciativas culturales"
            },
            {
                "title": "Apoyo al Deporte",
                "description": "Respaldo a campeonatos nacionales e internacionales en béisbol, ajedrez, damas, baloncesto, voleibol, fútbol y softball.",
                "impact": "Promoción del deporte y la actividad física en la comunidad.",
                "category_name": "Deportes",
                "image_src": "https://res.cloudinary.com/dwqkbu2e5/image/upload/v1/media/community/initiatives/sports-support.jpg",
                "image_alt": "Apoyo al deporte"
            }
        ]
        
        # Crear iniciativas
        initiatives_created = 0
        for initiative_data in initiatives_with_images:
            try:
                category = CommunityCategory.objects.get(name=initiative_data['category_name'])
                initiative, created = CommunityInitiative.objects.get_or_create(
                    title=initiative_data['title'],
                    defaults={
                        'description': initiative_data['description'],
                        'impact': initiative_data['impact'],
                        'category': category,
                        'image_src': initiative_data['image_src'],
                        'image_alt': initiative_data['image_alt'],
                        'is_active': True
                    }
                )
                if created:
                    initiatives_created += 1
                    self.stdout.write(f'  ✓ Iniciativa creada: {initiative.title}')
                else:
                    # Actualizar la iniciativa existente con las imágenes
                    try:
                        initiative.image_src = initiative_data['image_src']
                        initiative.image_alt = initiative_data['image_alt']
                        initiative.save()
                        self.stdout.write(f'  ✓ Iniciativa actualizada: {initiative.title}')
                    except Exception as e:
                        self.stdout.write(
                            self.style.WARNING(f'  ⚠ Iniciativa {initiative.title} no se pudo actualizar: {e}')
                        )
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
                f'\n✅ Datos creados exitosamente:\n'
                f'  - CommunitySupport: {"creado" if created else "actualizado"}\n'
                f'  - Categorías: {categories_created} nuevas\n'
                f'  - Iniciativas: {initiatives_created} nuevas'
            )
        )
