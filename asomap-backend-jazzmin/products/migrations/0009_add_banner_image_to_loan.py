# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_fix_loan_verbose_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='banner_image',
            field=models.ImageField(
                blank=True,
                help_text='Imagen principal del préstamo para el banner',
                null=True,
                upload_to='products/loans/',
                verbose_name='Imagen del banner'
            ),
        ),
    ]
