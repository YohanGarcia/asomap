"""
Comando de gestión para crear datos de ejemplo de memorias anuales
"""
from django.core.management.base import BaseCommand
from about.models import MemoryDocument, MemoryConfig


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para memorias anuales'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo para memorias anuales...')
        
        try:

            
            # Datos de memorias según el frontend
            memory_data = [
                {
                    'year': '2023',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2024/04/Memoria-ASOMAP-2023.pdf'
                },
                {
                    'year': '2022',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2023/04/INFORME-DE-GESTION-ANUAL2022.pdf'
                },
                {
                    'year': '2021',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2022/05/INFORME-DE-GESTION-ANUAL-2021-ARCHIVO-FINAL.pdf'
                },
                {
                    'year': '2020',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2022/05/MEMORIA-ANUAL-2020.pdf'
                },
                {
                    'year': '2018',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2020/02/Memoria-Asociaci%C3%B3n-Mocana-2018-1-VERSION-FINAL.pdf'
                },
                {
                    'year': '2017',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2022/05/Memoria-Asociaci%C3%B3n-Mocana-2017-ult.pdf'
                },
                {
                    'year': '2016',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2022/05/MEMORIA-ANUAL-2016.pdf'
                },
                {
                    'year': '2015',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2020/02/MEMORIA-ANUAL-2015.pdf'
                },
                {
                    'year': '2014',
                    'url': 'https://www.asomap.com.do/wp-content/uploads/2020/02/Memoria-2014.pdf'
                }
            ]
            
            # Crear documentos de memoria
            for data in memory_data:
                MemoryDocument.objects.get_or_create(
                    year=data['year'],
                    defaults={
                        'is_active': True
                    }
                )
            
            self.stdout.write(
                self.style.SUCCESS(
                    '✅ Datos de memorias anuales creados exitosamente:\n'
                    f'  - 1 configuración de memorias\n'
                    f'  - {len(memory_data)} años de memorias (2014-2023)\n'
                    f'  - Total: {len(memory_data)} documentos de memoria'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear datos de memorias: {e}')
            )
