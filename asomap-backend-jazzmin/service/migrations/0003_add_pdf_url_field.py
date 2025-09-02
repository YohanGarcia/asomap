# Generated manually for adding pdf_url field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_serviceinfo_servicespage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceinfo',
            name='pdf_url',
            field=models.URLField(
                blank=True,
                null=True,
                verbose_name='URL del PDF',
                help_text='URL externa del archivo PDF'
            ),
        ),
    ]
