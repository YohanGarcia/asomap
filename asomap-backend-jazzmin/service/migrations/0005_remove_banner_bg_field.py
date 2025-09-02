# Generated manually for removing banner_bg field

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_fix_pdf_url_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicespage',
            name='banner_bg',
        ),
    ]
