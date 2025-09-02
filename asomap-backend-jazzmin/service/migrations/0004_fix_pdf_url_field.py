# Generated manually for fixing pdf_url field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_add_pdf_url_field'),
    ]

    operations = [
        # Asegurar que el campo pdf_url existe y está correctamente configurado
        migrations.AlterField(
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
