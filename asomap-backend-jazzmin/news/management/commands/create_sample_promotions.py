"""
Comando de gestión para crear promociones de ejemplo
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from news.models import Promotion


class Command(BaseCommand):
    help = 'Crea promociones de ejemplo para el frontend'

    def handle(self, *args, **options):
        self.stdout.write('Creando promociones de ejemplo...')
        
        promotions_data = [
            {
                'title': 'Descuento especial para nuevos clientes',
                'description': 'Aprovecha nuestro descuento especial del 50% en comisiones por apertura de cuenta para nuevos clientes.',
                'category': 'Descuentos',
                'tags': 'Nuevo cliente, Descuento, Comisiones',
                'full_content': '''
                    <p>Aprovecha nuestro descuento especial del 50% en comisiones por apertura de cuenta para nuevos clientes.</p>
                    
                    <h2>Beneficios de la promoción</h2>
                    
                    <ul>
                        <li>50% de descuento en comisiones de apertura</li>
                        <li>Sin costo de mantenimiento por 6 meses</li>
                        <li>Tarjeta de débito gratis</li>
                        <li>Acceso inmediato a banca en línea</li>
                    </ul>
                    
                    <blockquote>¡Únete a ASOMAP y disfruta de beneficios exclusivos desde el primer día!</blockquote>
                    
                    <p>Esta promoción está diseñada para facilitar el acceso a servicios financieros de calidad a nuevos clientes.</p>
                ''',
                'terms': 'Válido solo para nuevos clientes, No aplica con otras promociones, Sujeto a aprobación crediticia, La promoción puede ser modificada sin previo aviso, Válido hasta agotar existencias',
                'media_urls': 'https://images.unsplash.com/photo-1560472355-536de3962603?q=80&w=1200',
                'related_links': 'https://asomap.com/nuevos-clientes',
                'fecha_inicio': timezone.now().date(),
                'fecha_fin': timezone.now().date() + timedelta(days=90)
            },
            {
                'title': 'Préstamo personal con tasa preferencial',
                'description': 'Obtén un préstamo personal con una tasa de interés preferencial del 12% anual para clientes con buen historial crediticio.',
                'category': 'Préstamos',
                'tags': 'Préstamo personal, Tasa preferencial, Cliente existente',
                'full_content': '''
                    <p>Obtén un préstamo personal con una tasa de interés preferencial del 12% anual para clientes con buen historial crediticio.</p>
                    
                    <h2>Características del préstamo</h2>
                    
                    <ul>
                        <li>Tasa de interés preferencial del 12% anual</li>
                        <li>Monto desde RD$ 50,000 hasta RD$ 2,000,000</li>
                        <li>Plazos de 12 a 60 meses</li>
                        <li>Sin garantía hipotecaria</li>
                        <li>Desembolso en 24 horas</li>
                    </ul>
                    
                    <p>Esta promoción está disponible exclusivamente para clientes con al menos 6 meses de antigüedad y buen historial crediticio.</p>
                ''',
                'terms': 'Solo para clientes existentes, Sujeto a aprobación crediticia, Requiere buen historial crediticio, Mínimo 6 meses de antigüedad, La promoción puede ser modificada sin previo aviso',
                'fecha_inicio': timezone.now().date(),
                'fecha_fin': timezone.now().date() + timedelta(days=180)
            },
            {
                'title': 'Tarjeta de crédito sin anualidad por 2 años',
                'description': 'Obtén nuestra tarjeta de crédito premium sin pagar anualidad durante los primeros 2 años.',
                'category': 'Tarjetas',
                'tags': 'Tarjeta de crédito, Sin anualidad, Premium',
                'full_content': '''
                    <p>Obtén nuestra tarjeta de crédito premium sin pagar anualidad durante los primeros 2 años.</p>
                    
                    <h2>Beneficios de la tarjeta premium</h2>
                    
                    <ul>
                        <li>Sin anualidad por 2 años</li>
                        <li>Línea de crédito desde RD$ 100,000</li>
                        <li>Puntos de recompensa en todas las compras</li>
                        <li>Seguro de compras y viajes incluido</li>
                        <li>Acceso a salas VIP en aeropuertos</li>
                    </ul>
                    
                    <blockquote>Disfruta de los beneficios premium sin costo durante 2 años</blockquote>
                    
                    <p>Esta promoción está diseñada para clientes con ingresos superiores a RD$ 50,000 mensuales.</p>
                ''',
                'terms': 'Ingresos mínimos RD$ 50,000 mensuales, Sujeto a aprobación crediticia, Requiere documentación completa, La promoción puede ser modificada sin previo aviso, Válido hasta el 31 de diciembre de 2024',
                'fecha_inicio': timezone.now().date(),
                'fecha_fin': datetime(2024, 12, 31).date()
            }
        ]
        
        created_count = 0
        for i, promotion_item in enumerate(promotions_data):
            promotion, created = Promotion.objects.get_or_create(
                title=promotion_item['title'],
                defaults={
                    'description': promotion_item['description'],
                    'category': promotion_item['category'],
                    'tags': promotion_item['tags'],
                    'full_content': promotion_item['full_content'].strip(),
                    'terms': promotion_item['terms'],
                    'media_urls': promotion_item.get('media_urls', ''),
                    'related_links': promotion_item.get('related_links', ''),
                    'fecha_inicio': promotion_item['fecha_inicio'],
                    'fecha_fin': promotion_item['fecha_fin'],
                    'is_active': True
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'✓ Promoción "{promotion_item["title"]}" creada')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} promociones de ejemplo creadas exitosamente'
            )
        )
