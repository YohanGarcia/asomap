from django.core.management.base import BaseCommand
from layout.models import SocialNetwork, Contact


class Command(BaseCommand):
    help = 'Crea datos iniciales para redes sociales y contactos'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Creando datos iniciales para layout...')

        # Crear redes sociales
        social_networks_data = [
            {
                'name': 'Facebook',
                'url': 'https://www.facebook.com/asomap',
                'icon': 'FaFacebook',
                'order': 1
            },
            {
                'name': 'Instagram',
                'url': 'https://www.instagram.com/asomap',
                'icon': 'FaInstagram',
                'order': 2
            },
            {
                'name': 'Twitter',
                'url': 'https://www.twitter.com/asomap',
                'icon': 'FaTwitter',
                'order': 3
            },
            {
                'name': 'LinkedIn',
                'url': 'https://www.linkedin.com/company/asomap',
                'icon': 'FaLinkedin',
                'order': 4
            },
            {
                'name': 'YouTube',
                'url': 'https://www.youtube.com/asomap',
                'icon': 'FaYoutube',
                'order': 5
            }
        ]

        for data in social_networks_data:
            social_network, created = SocialNetwork.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            if created:
                self.stdout.write(f'✅ Red social creada: {data["name"]}')
            else:
                self.stdout.write(f'⚠️  Red social ya existe: {data["name"]}')

        # Crear contactos
        contacts_data = [
            {
                'name': 'Teléfono Principal',
                'url': 'tel:+18091234567',
                'icon': 'FaPhone',
                'order': 1
            },
            {
                'name': 'Email General',
                'url': 'mailto:info@asomap.com',
                'icon': 'FaEnvelope',
                'order': 2
            },
            {
                'name': 'WhatsApp',
                'url': 'https://wa.me/18091234567',
                'icon': 'FaWhatsapp',
                'order': 3
            },
            {
                'name': 'Dirección Principal',
                'url': 'https://maps.google.com/?q=ASOMAP+Santo+Domingo',
                'icon': 'FaMapMarkerAlt',
                'order': 4
            },
            {
                'name': 'Horarios de Atención',
                'url': 'tel:+18091234567',
                'icon': 'FaClock',
                'order': 5
            }
        ]

        for data in contacts_data:
            contact, created = Contact.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            if created:
                self.stdout.write(f'✅ Contacto creado: {data["name"]}')
            else:
                self.stdout.write(f'⚠️  Contacto ya existe: {data["name"]}')

        self.stdout.write(
            self.style.SUCCESS('🎉 ¡Datos iniciales creados exitosamente!')
        )
        self.stdout.write('📱 Puedes gestionar las redes sociales y contactos desde el panel de administración.')
