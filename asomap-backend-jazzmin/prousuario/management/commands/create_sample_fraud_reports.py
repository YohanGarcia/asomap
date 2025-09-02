from django.core.management.base import BaseCommand
from prousuario.models import FraudReport


class Command(BaseCommand):
    help = 'Crea reportes de fraude de muestra para pruebas'

    def handle(self, *args, **options):
        self.stdout.write('Creando reportes de fraude de muestra...')

        # Datos de muestra
        sample_reports = [
            {
                'full_name': 'María González López',
                'document': '402-1234567-8',
                'phone': '809-555-0101',
                'email': 'maria.gonzalez@email.com',
                'classification': 'Phishing',
                'message': 'Recibí un email sospechoso que parece ser de ASOMAP solicitando información personal. El email tiene errores gramaticales y el enlace parece falso.',
                'status': 'pending'
            },
            {
                'full_name': 'Carlos Rodríguez Pérez',
                'document': '402-9876543-2',
                'phone': '809-555-0202',
                'email': 'carlos.rodriguez@email.com',
                'classification': 'Fraude de Tarjeta',
                'message': 'Noté cargos en mi tarjeta de débito que no reconozco. Los cargos aparecen en comercios que no he visitado y fechas en las que no usé la tarjeta.',
                'status': 'in_progress'
            },
            {
                'full_name': 'Ana Martínez Silva',
                'document': '402-4567890-1',
                'phone': '809-555-0303',
                'email': 'ana.martinez@email.com',
                'classification': 'Robo de Identidad',
                'message': 'Descubrí que alguien está usando mi información personal para abrir cuentas a mi nombre. Recibí notificaciones de créditos que no solicité.',
                'status': 'resolved'
            },
            {
                'full_name': 'Luis Fernández Torres',
                'document': '402-7890123-4',
                'phone': '809-555-0404',
                'email': 'luis.fernandez@email.com',
                'classification': 'Toma de Cuenta',
                'message': 'No puedo acceder a mi cuenta en línea. Parece que alguien cambió mi contraseña y mi número de teléfono asociado.',
                'status': 'pending'
            },
            {
                'full_name': 'Isabel Sánchez Ruiz',
                'document': '402-3210987-6',
                'phone': '809-555-0505',
                'email': 'isabel.sanchez@email.com',
                'classification': 'Lavado de Dinero',
                'message': 'Observé transferencias sospechosas en mi cuenta que no realicé. Las cantidades son inusuales y los destinatarios no los reconozco.',
                'status': 'in_progress'
            }
        ]

        created_count = 0
        for report_data in sample_reports:
            report, created = FraudReport.objects.get_or_create(
                email=report_data['email'],
                defaults=report_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✅ Reporte creado: {report.full_name} - {report.classification}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'⚠️ Reporte ya existe: {report.full_name}'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n🎉 Proceso completado. {created_count} reportes de fraude creados.'
            )
        )
