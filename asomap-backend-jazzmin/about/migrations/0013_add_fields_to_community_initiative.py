# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # Ajuste: en el contenedor no existe 0012 aún; encadenamos desde 0011
        ('about', '0011_alter_mision_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityinitiative',
            name='year',
            field=models.IntegerField(
                help_text='Año en que se realizó la iniciativa',
                verbose_name='Año',
                null=True,
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name='communityinitiative',
            name='location',
            field=models.CharField(
                help_text='Nombre de la ubicación donde se realizó la iniciativa',
                max_length=200,
                verbose_name='Ubicación',
                null=True,
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name='communityinitiative',
            name='beneficiaries',
            field=models.CharField(
                help_text='Descripción de los beneficiarios de la iniciativa',
                max_length=200,
                verbose_name='Beneficiarios',
                null=True,
                blank=True,
            ),
        ),
    ]
