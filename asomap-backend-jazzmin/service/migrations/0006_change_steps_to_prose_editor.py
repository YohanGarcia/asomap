# Generated manually for changing steps field to ProseEditorField

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_remove_banner_bg_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceinfo',
            name='steps',
            field=models.TextField(
                blank=True,
                verbose_name='Pasos',
                help_text='Pasos para usar el servicio (puedes usar listas con viñetas)'
            ),
        ),
    ]
