"""
Comando de gestión para crear noticias de ejemplo
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from news.models import News


class Command(BaseCommand):
    help = 'Crea noticias de ejemplo para el frontend'

    def handle(self, *args, **options):
        self.stdout.write('Creando noticias de ejemplo...')
        
        news_data = [
            {
                'title': 'ASOMAP celebra su 60 aniversario',
                'description': 'La Asociación Popular de Ahorros y Préstamos (ASOMAP) celebró su 60 aniversario con una serie de eventos especiales que resaltaron su trayectoria de servicio y compromiso con la comunidad dominicana.',
                'author': 'Equipo de Comunicaciones ASOMAP',
                'category': 'Eventos Institucionales',
                'tags': 'Aniversario, Celebración, Historia',
                'full_content': '''
                    <p>La Asociación Popular de Ahorros y Préstamos (ASOMAP) celebró su 60 aniversario con una serie de eventos especiales que resaltaron su trayectoria de servicio y compromiso con la comunidad dominicana.</p>
                    
                    <h2>Un legado de servicio a la comunidad</h2>
                    
                    <p>Durante seis décadas, ASOMAP ha sido un pilar fundamental en el desarrollo económico y social de la República Dominicana, ofreciendo servicios financieros accesibles y de calidad a miles de familias dominicanas.</p>
                    
                    <ul>
                        <li>Más de 100,000 familias beneficiadas</li>
                        <li>Presencia en 15 provincias del país</li>
                        <li>Compromiso con la inclusión financiera</li>
                    </ul>
                    
                    <blockquote>Nuestro compromiso es seguir sirviendo a la comunidad dominicana con excelencia y dedicación.</blockquote>
                ''',
                'media_urls': 'https://images.unsplash.com/photo-1560472355-536de3962603?q=80&w=1200',
                'related_links': 'https://asomap.com/historia'
            },
            {
                'title': 'Nueva sucursal en Santiago de los Caballeros',
                'description': 'ASOMAP inaugura su nueva sucursal en Santiago de los Caballeros, ampliando su presencia en la región norte del país.',
                'author': 'Departamento de Expansión',
                'category': 'Expansión',
                'tags': 'Sucursal, Santiago, Expansión',
                'full_content': '''
                    <p>ASOMAP inaugura su nueva sucursal en Santiago de los Caballeros, ampliando su presencia en la región norte del país y fortaleciendo su compromiso con el desarrollo regional.</p>
                    
                    <h2>Servicios disponibles en la nueva sucursal</h2>
                    
                    <ul>
                        <li>Apertura de cuentas de ahorro</li>
                        <li>Préstamos personales y comerciales</li>
                        <li>Servicios de cajero automático</li>
                        <li>Atención al cliente especializada</li>
                    </ul>
                    
                    <p>La nueva sucursal está ubicada en el corazón de Santiago y cuenta con tecnología de vanguardia para ofrecer el mejor servicio a nuestros asociados.</p>
                ''',
                'media_urls': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=80&w=1200'
            },
            {
                'title': 'Programa de microcréditos para emprendedores',
                'description': 'ASOMAP lanza un nuevo programa de microcréditos diseñado específicamente para apoyar a emprendedores y pequeños negocios.',
                'author': 'Departamento de Créditos',
                'category': 'Productos y Servicios',
                'tags': 'Microcréditos, Emprendedores, Apoyo',
                'full_content': '''
                    <p>ASOMAP lanza un nuevo programa de microcréditos diseñado específicamente para apoyar a emprendedores y pequeños negocios en su crecimiento y desarrollo.</p>
                    
                    <h2>Características del programa</h2>
                    
                    <ul>
                        <li>Préstamos desde RD$ 10,000 hasta RD$ 500,000</li>
                        <li>Tasas de interés preferenciales</li>
                        <li>Plazos flexibles de hasta 36 meses</li>
                        <li>Documentación simplificada</li>
                    </ul>
                    
                    <blockquote>Nuestro compromiso es impulsar el desarrollo económico local a través del apoyo a emprendedores</blockquote>
                    
                    <p>Este programa representa nuestro compromiso con el desarrollo económico local y la inclusión financiera de pequeños empresarios.</p>
                '''
            }
        ]
        
        created_count = 0
        for i, news_item in enumerate(news_data):
            # Crear fechas de publicación escalonadas
            fecha_publicacion = timezone.now() - timedelta(days=i*7)
            
            news, created = News.objects.get_or_create(
                title=news_item['title'],
                defaults={
                    'description': news_item['description'],
                    'author': news_item['author'],
                    'category': news_item['category'],
                    'tags': news_item['tags'],
                    'full_content': news_item['full_content'].strip(),
                    'media_urls': news_item.get('media_urls', ''),
                    'related_links': news_item.get('related_links', ''),
                    'fecha_publicacion': fecha_publicacion,
                    'is_active': True
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'✓ Noticia "{news_item["title"]}" creada')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} noticias de ejemplo creadas exitosamente'
            )
        ) 