from django.core.management.base import BaseCommand
from prousuario.models import Province


class Command(BaseCommand):
    help = 'Crea las provincias de República Dominicana'

    def handle(self, *args, **options):
        self.stdout.write('Creando provincias de República Dominicana...')
        
        # Lista de provincias de RD
        provinces_data = [
            'Azua',
            'Baoruco',
            'Barahona',
            'Dajabón',
            'Distrito Nacional',
            'Duarte',
            'Elías Piña',
            'El Seibo',
            'Espaillat',
            'Hato Mayor',
            'Hermanas Mirabal',
            'Independencia',
            'La Altagracia',
            'La Romana',
            'La Vega',
            'María Trinidad Sánchez',
            'Monseñor Nouel',
            'Monte Cristi',
            'Monte Plata',
            'Pedernales',
            'Peravia',
            'Puerto Plata',
            'Samaná',
            'San Cristóbal',
            'San José de Ocoa',
            'San Juan',
            'San Pedro de Macorís',
            'Sánchez Ramírez',
            'Santiago',
            'Santiago Rodríguez',
            'Santo Domingo',
            'Valverde',
        ]
        
        created_count = 0
        updated_count = 0
        
        for province_name in provinces_data:
            province, created = Province.objects.get_or_create(
                name=province_name,
                defaults={
                    'is_active': True
                }
            )
            
            if created:
                self.stdout.write(f'✅ Provincia creada: {province.name}')
                created_count += 1
            else:
                # Actualizar si ya existe
                province.is_active = True
                province.save()
                self.stdout.write(f'🔄 Provincia actualizada: {province.name}')
                updated_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Proceso completado. {created_count} provincias creadas, {updated_count} actualizadas.'
            )
        )
