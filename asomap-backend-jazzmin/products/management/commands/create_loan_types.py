from django.core.management.base import BaseCommand
from products.models import LoanType

class Command(BaseCommand):
    help = 'Crea los tipos de préstamos iniciales'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forzar la creación incluso si ya existen tipos de préstamos',
        )

    def handle(self, *args, **options):
        self.stdout.write('Creando tipos de préstamos iniciales...')
        
        loan_types_data = [
            {
                'name': 'Compra de vivienda',
                'slug': 'compra-de-vivienda',
                'description': 'Préstamo para la compra de una vivienda nueva o usada',
                'is_active': True,
                'order': 1
            },
            {
                'name': 'Ampliación o remodelación',
                'slug': 'ampliacion-o-remodelacion',
                'description': 'Préstamo para ampliar o remodelar tu vivienda actual',
                'is_active': True,
                'order': 2
            },
            {
                'name': 'Construcción',
                'slug': 'construccion',
                'description': 'Préstamo para construir tu vivienda desde cero',
                'is_active': True,
                'order': 3
            },
            {
                'name': 'Compra de terreno',
                'slug': 'compra-de-terreno',
                'description': 'Préstamo para la compra de un terreno',
                'is_active': True,
                'order': 4
            },
            {
                'name': 'Préstamo de Consumo',
                'slug': 'prestamo-de-consumo',
                'description': 'Préstamo para gastos personales y consumo',
                'is_active': True,
                'order': 5
            },
        ]
        
        created_count = 0
        updated_count = 0
        
        for loan_type_data in loan_types_data:
            loan_type, created = LoanType.objects.get_or_create(
                slug=loan_type_data['slug'],
                defaults=loan_type_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(f'✓ Tipo de préstamo "{loan_type_data["name"]}" creado')
            else:
                if options['force']:
                    # Actualizar datos existentes
                    for key, value in loan_type_data.items():
                        if key != 'slug':  # No actualizar el slug
                            setattr(loan_type, key, value)
                    loan_type.save()
                    updated_count += 1
                    self.stdout.write(f'✓ Tipo de préstamo "{loan_type_data["name"]}" actualizado')
                else:
                    self.stdout.write(f'⚠️  Tipo de préstamo "{loan_type_data["name"]}" ya existe, saltando...')
        
        if created_count > 0 or updated_count > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Tipos de préstamos procesados exitosamente: {created_count} creados, {updated_count} actualizados'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    '⚠️  No se crearon ni actualizaron tipos de préstamos. Usa --force para actualizar los existentes.'
                )
            )
