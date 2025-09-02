"""
Comando de gestión para crear datos de ejemplo de políticas organizacionales
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from about.models import PolicyDocument, PolicyCategory, PolicyConfig


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para políticas organizacionales'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo para políticas organizacionales...')
        
        try:
            # Crear configuración de políticas
            config = PolicyConfig.objects.get_or_create(
                defaults={
                    'title': "Políticas",
                    'description': "Nuestras políticas institucionales garantizan la transparencia y eficiencia en nuestras operaciones.",
                    'download_text': "Descargar documento",
                    'last_update_text': "Última actualización",
                    'all_policies_text': "Todas las Políticas",
                    'is_active': True
                }
            )[0]
            
            # Crear categorías de políticas
            categories_data = [
                {
                    'title': "Políticas de Gobernanza",
                    'icon': "shield",
                    'description': "Lineamientos fundamentales que rigen nuestra institución",
                    'documents': [
                        {
                            'title': "Código de Ética y Conducta",
                            'description': "Lineamientos éticos y conductuales para todos los miembros de la institución",
                            'last_update': date(2024, 1, 15)
                        },
                        {
                            'title': "Política de Gobierno Corporativo",
                            'description': "Marco de gobierno y toma de decisiones institucional",
                            'last_update': date(2023, 12, 1)
                        },
                        {
                            'title': "Política de Transparencia",
                            'description': "Directrices para garantizar la transparencia en todas nuestras operaciones",
                            'last_update': date(2024, 1, 20)
                        },
                        {
                            'title': "Manual de Gobernanza Digital",
                            'description': "Guía para la gestión de activos y procesos digitales",
                            'last_update': date(2024, 1, 18)
                        }
                    ]
                },
                {
                    'title': "Políticas Operativas",
                    'icon': "cog",
                    'description': "Procedimientos y normas para nuestras operaciones diarias",
                    'documents': [
                        {
                            'title': "Manual de Procedimientos",
                            'description': "Procedimientos operativos estándar de la institución",
                            'last_update': date(2024, 1, 10)
                        },
                        {
                            'title': "Política de Seguridad",
                            'description': "Normas y procedimientos de seguridad institucional",
                            'last_update': date(2023, 11, 15)
                        },
                        {
                            'title': "Manual de Calidad",
                            'description': "Estándares y procesos para asegurar la calidad del servicio",
                            'last_update': date(2024, 1, 22)
                        },
                        {
                            'title': "Política de Gestión de Riesgos",
                            'description': "Marco para la identificación y gestión de riesgos operativos",
                            'last_update': date(2024, 1, 5)
                        },
                        {
                            'title': "Manual de Continuidad de Negocio",
                            'description': "Procedimientos para garantizar la continuidad operativa",
                            'last_update': date(2024, 1, 12)
                        }
                    ]
                },
                {
                    'title': "Políticas de Cumplimiento",
                    'icon': "check-circle",
                    'description': "Normativas y regulaciones que aseguran nuestro cumplimiento",
                    'documents': [
                        {
                            'title': "Manual de Prevención de Lavado",
                            'description': "Políticas y procedimientos contra el lavado de activos",
                            'last_update': date(2024, 1, 5)
                        },
                        {
                            'title': "Política de Protección al Usuario",
                            'description': "Lineamientos para la protección de nuestros usuarios",
                            'last_update': date(2023, 12, 20)
                        },
                        {
                            'title': "Política de Privacidad de Datos",
                            'description': "Normas para la protección y manejo de datos personales",
                            'last_update': date(2024, 1, 25)
                        },
                        {
                            'title': "Manual de Cumplimiento Regulatorio",
                            'description': "Guía para el cumplimiento de regulaciones financieras",
                            'last_update': date(2024, 1, 15)
                        },
                        {
                            'title': "Política Antisoborno y Anticorrupción",
                            'description': "Medidas preventivas contra el soborno y la corrupción",
                            'last_update': date(2024, 1, 8)
                        },
                        {
                            'title': "Manual de Debida Diligencia",
                            'description': "Procedimientos para la evaluación de clientes y proveedores",
                            'last_update': date(2024, 1, 19)
                        }
                    ]
                }
            ]
            
            total_documents = 0
            
            for category_data in categories_data:
                # Crear categoría
                category = PolicyCategory.objects.get_or_create(
                    title=category_data['title'],
                    defaults={
                        'icon': category_data['icon'],
                        'description': category_data['description'],
                        'is_active': True
                    }
                )[0]
                
                # Crear documentos para la categoría
                for doc_data in category_data['documents']:
                    document = PolicyDocument.objects.get_or_create(
                        title=doc_data['title'],
                        defaults={
                            'description': doc_data['description'],
                            'last_update': doc_data['last_update'],
                            'is_active': True
                        }
                    )[0]
                    
                    # Asociar documento con la categoría
                    category.documents.add(document)
                    total_documents += 1
            
            self.stdout.write(
                self.style.SUCCESS(
                    '✅ Datos de políticas organizacionales creados exitosamente:\n'
                    f'  - 1 configuración de políticas\n'
                    f'  - {len(categories_data)} categorías de políticas\n'
                    f'  - {total_documents} documentos de políticas\n'
                    f'  - Total: {total_documents + len(categories_data) + 1} elementos'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear datos de políticas: {e}')
            )
