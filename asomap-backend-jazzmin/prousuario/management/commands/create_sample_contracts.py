from django.core.management.base import BaseCommand
from prousuario.models import ContractCategory, AccountContractsSection, Contract


class Command(BaseCommand):
    help = 'Crea datos de muestra para contratos de adhesión'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de muestra para contratos de adhesión...')
        
        # Crear categorías
        categories_data = [
            "Cuentas",
            "Préstamos", 
            "Pagarés",
            "Servicios",
            "Tarjetas"
        ]
        
        categories = {}
        for cat_name in categories_data:
            category, created = ContractCategory.objects.get_or_create(
                name=cat_name,
                defaults={'is_active': True}
            )
            categories[cat_name] = category
            if created:
                self.stdout.write(f'✓ Categoría creada: {category.name}')
            else:
                self.stdout.write(f'✓ Categoría ya existía: {category.name}')
        
        # Crear sección principal
        section, created = AccountContractsSection.objects.get_or_create(
            title='Contratos de adhesión',
            defaults={
                'description': 'Documentos legales que establecen los términos y condiciones de nuestros servicios.',
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(f'✓ Sección creada: {section.title}')
        else:
            self.stdout.write(f'✓ Sección ya existía: {section.title}')
        
        # Crear contratos de muestra (sin archivos, solo estructura)
        contracts_data = [
            {
                'title': "Contrato Cuenta de Ahorro Persona Física",
                'category': "Cuentas"
            },
            {
                'title': "Contrato Cuenta de Ahorro Persona Jurídica",
                'category': "Cuentas"
            },
            {
                'title': "Contrato San Ideal",
                'category': "Cuentas"
            },
            {
                'title': "Contrato Préstamo Garantizado",
                'category': "Préstamos"
            },
            {
                'title': "Contrato de Préstamo Hipotecario",
                'category': "Préstamos"
            },
            {
                'title': "Pagaré a la Orden",
                'category': "Pagarés"
            },
            {
                'title': "Pagaré Comercial",
                'category': "Pagarés"
            },
            {
                'title': "Contrato Caja de Seguridad",
                'category': "Servicios"
            },
            {
                'title': "Contrato de Tarjeta de Débito",
                'category': "Tarjetas"
            }
        ]
        
        contracts_created = 0
        for i, contract_info in enumerate(contracts_data):
            contract, created = Contract.objects.get_or_create(
                title=contract_info['title'],
                defaults={
                    'category': categories[contract_info['category']],
                    'order': i + 1,
                    'is_active': True
                }
            )
            
            if created:
                contracts_created += 1
        
        self.stdout.write(f'✓ {contracts_created} contratos de muestra creados')
        self.stdout.write(self.style.SUCCESS('¡Datos de muestra de contratos creados exitosamente!'))
        
        # Mostrar resumen
        self.stdout.write('\nResumen:')
        self.stdout.write(f'- Categorías: {ContractCategory.objects.count()}')
        self.stdout.write(f'- Secciones: {AccountContractsSection.objects.count()}')
        self.stdout.write(f'- Contratos: {Contract.objects.count()}')
