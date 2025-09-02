"""
Comando de gestión para crear horarios predefinidos
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import time
from locations.models import Schedule


class Command(BaseCommand):
    help = 'Crea horarios predefinidos para las ubicaciones'

    def handle(self, *args, **options):
        self.stdout.write('Creando horarios predefinidos...')
        
        schedules_data = [
            # Horarios tempranos
            {'name': '6:00 AM - 4:00 PM', 'opening_time': time(6, 0), 'closing_time': time(16, 0), 'is_24_7': False},
            {'name': '6:30 AM - 4:00 PM', 'opening_time': time(6, 30), 'closing_time': time(16, 0), 'is_24_7': False},
            {'name': '7:00 AM - 4:00 PM', 'opening_time': time(7, 0), 'closing_time': time(16, 0), 'is_24_7': False},
            {'name': '7:30 AM - 4:00 PM', 'opening_time': time(7, 30), 'closing_time': time(16, 0), 'is_24_7': False},
            
            # Horarios estándar mañana
            {'name': '8:00 AM - 4:00 PM', 'opening_time': time(8, 0), 'closing_time': time(16, 0), 'is_24_7': False},
            {'name': '8:00 AM - 4:30 PM', 'opening_time': time(8, 0), 'closing_time': time(16, 30), 'is_24_7': False},
            {'name': '8:00 AM - 5:00 PM', 'opening_time': time(8, 0), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': '8:30 AM - 4:00 PM', 'opening_time': time(8, 30), 'closing_time': time(16, 0), 'is_24_7': False},
            {'name': '8:30 AM - 4:30 PM', 'opening_time': time(8, 30), 'closing_time': time(16, 30), 'is_24_7': False},
            {'name': '8:30 AM - 5:00 PM', 'opening_time': time(8, 30), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': '8:30 AM - 5:30 PM', 'opening_time': time(8, 30), 'closing_time': time(17, 30), 'is_24_7': False},
            
            # Horarios estándar tarde
            {'name': '9:00 AM - 4:00 PM', 'opening_time': time(9, 0), 'closing_time': time(16, 0), 'is_24_7': False},
            {'name': '9:00 AM - 4:30 PM', 'opening_time': time(9, 0), 'closing_time': time(16, 30), 'is_24_7': False},
            {'name': '9:00 AM - 5:00 PM', 'opening_time': time(9, 0), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': '9:00 AM - 5:30 PM', 'opening_time': time(9, 0), 'closing_time': time(17, 30), 'is_24_7': False},
            {'name': '9:00 AM - 6:00 PM', 'opening_time': time(9, 0), 'closing_time': time(18, 0), 'is_24_7': False},
            {'name': '9:30 AM - 5:00 PM', 'opening_time': time(9, 30), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': '9:30 AM - 5:30 PM', 'opening_time': time(9, 30), 'closing_time': time(17, 30), 'is_24_7': False},
            {'name': '9:30 AM - 6:00 PM', 'opening_time': time(9, 30), 'closing_time': time(18, 0), 'is_24_7': False},
            
            # Horarios extendidos
            {'name': '8:00 AM - 6:00 PM', 'opening_time': time(8, 0), 'closing_time': time(18, 0), 'is_24_7': False},
            {'name': '8:30 AM - 6:00 PM', 'opening_time': time(8, 30), 'closing_time': time(18, 0), 'is_24_7': False},
            {'name': '8:30 AM - 6:30 PM', 'opening_time': time(8, 30), 'closing_time': time(18, 30), 'is_24_7': False},
            {'name': '9:00 AM - 6:30 PM', 'opening_time': time(9, 0), 'closing_time': time(18, 30), 'is_24_7': False},
            {'name': '9:00 AM - 7:00 PM', 'opening_time': time(9, 0), 'closing_time': time(19, 0), 'is_24_7': False},
            
            # Horarios muy tempranos
            {'name': '5:00 AM - 3:00 PM', 'opening_time': time(5, 0), 'closing_time': time(15, 0), 'is_24_7': False},
            {'name': '5:30 AM - 3:00 PM', 'opening_time': time(5, 30), 'closing_time': time(15, 0), 'is_24_7': False},
            {'name': '5:30 AM - 3:30 PM', 'opening_time': time(5, 30), 'closing_time': time(15, 30), 'is_24_7': False},
            {'name': '6:00 AM - 3:00 PM', 'opening_time': time(6, 0), 'closing_time': time(15, 0), 'is_24_7': False},
            {'name': '6:00 AM - 3:30 PM', 'opening_time': time(6, 0), 'closing_time': time(15, 30), 'is_24_7': False},
            
            # Horarios tarde
            {'name': '10:00 AM - 6:00 PM', 'opening_time': time(10, 0), 'closing_time': time(18, 0), 'is_24_7': False},
            {'name': '10:00 AM - 6:30 PM', 'opening_time': time(10, 0), 'closing_time': time(18, 30), 'is_24_7': False},
            {'name': '10:00 AM - 7:00 PM', 'opening_time': time(10, 0), 'closing_time': time(19, 0), 'is_24_7': False},
            {'name': '10:30 AM - 6:00 PM', 'opening_time': time(10, 30), 'closing_time': time(18, 0), 'is_24_7': False},
            {'name': '10:30 AM - 6:30 PM', 'opening_time': time(10, 30), 'closing_time': time(18, 30), 'is_24_7': False},
            {'name': '10:30 AM - 7:00 PM', 'opening_time': time(10, 30), 'closing_time': time(19, 0), 'is_24_7': False},
            
            # Horarios nocturnos
            {'name': '11:00 AM - 7:00 PM', 'opening_time': time(11, 0), 'closing_time': time(19, 0), 'is_24_7': False},
            {'name': '11:00 AM - 8:00 PM', 'opening_time': time(11, 0), 'closing_time': time(20, 0), 'is_24_7': False},
            {'name': '12:00 PM - 8:00 PM', 'opening_time': time(12, 0), 'closing_time': time(20, 0), 'is_24_7': False},
            {'name': '1:00 PM - 9:00 PM', 'opening_time': time(13, 0), 'closing_time': time(21, 0), 'is_24_7': False},
            {'name': '2:00 PM - 10:00 PM', 'opening_time': time(14, 0), 'closing_time': time(22, 0), 'is_24_7': False},
            
            # Horarios muy extendidos
            {'name': '6:00 AM - 10:00 PM', 'opening_time': time(6, 0), 'closing_time': time(22, 0), 'is_24_7': False},
            {'name': '7:00 AM - 10:00 PM', 'opening_time': time(7, 0), 'closing_time': time(22, 0), 'is_24_7': False},
            {'name': '7:00 AM - 11:00 PM', 'opening_time': time(7, 0), 'closing_time': time(23, 0), 'is_24_7': False},
            {'name': '8:00 AM - 10:00 PM', 'opening_time': time(8, 0), 'closing_time': time(22, 0), 'is_24_7': False},
            {'name': '8:00 AM - 11:00 PM', 'opening_time': time(8, 0), 'closing_time': time(23, 0), 'is_24_7': False},
            
            # Horarios especiales
            {'name': '24/7', 'opening_time': time(0, 0), 'closing_time': time(23, 59), 'is_24_7': True},
            {'name': '6:00 AM - 12:00 AM', 'opening_time': time(6, 0), 'closing_time': time(0, 0), 'is_24_7': False},
            {'name': '7:00 AM - 12:00 AM', 'opening_time': time(7, 0), 'closing_time': time(0, 0), 'is_24_7': False},
            {'name': '8:00 AM - 12:00 AM', 'opening_time': time(8, 0), 'closing_time': time(0, 0), 'is_24_7': False},
            
            # Horarios de fin de semana
            {'name': 'Lunes a Viernes 8:00 AM - 5:00 PM', 'opening_time': time(8, 0), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': 'Lunes a Viernes 8:30 AM - 5:00 PM', 'opening_time': time(8, 30), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': 'Lunes a Viernes 9:00 AM - 6:00 PM', 'opening_time': time(9, 0), 'closing_time': time(18, 0), 'is_24_7': False},
            {'name': 'Lunes a Viernes 9:00 AM - 5:30 PM', 'opening_time': time(9, 0), 'closing_time': time(17, 30), 'is_24_7': False},
            {'name': 'Lunes a Sábado 8:00 AM - 5:00 PM', 'opening_time': time(8, 0), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': 'Lunes a Sábado 8:30 AM - 5:00 PM', 'opening_time': time(8, 30), 'closing_time': time(17, 0), 'is_24_7': False},
            {'name': 'Lunes a Sábado 9:00 AM - 6:00 PM', 'opening_time': time(9, 0), 'closing_time': time(18, 0), 'is_24_7': False},
            {'name': 'Lunes a Sábado 9:00 AM - 5:30 PM', 'opening_time': time(9, 0), 'closing_time': time(17, 30), 'is_24_7': False},
        ]
        
        created_count = 0
        for schedule_data in schedules_data:
            schedule, created = Schedule.objects.get_or_create(
                name=schedule_data['name'],
                defaults={
                    'opening_time': schedule_data['opening_time'],
                    'closing_time': schedule_data['closing_time'],
                    'is_24_7': schedule_data['is_24_7'],
                    'is_active': True
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'✓ Horario "{schedule_data["name"]}" creado')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {created_count} horarios predefinidos creados exitosamente'
            )
        )
