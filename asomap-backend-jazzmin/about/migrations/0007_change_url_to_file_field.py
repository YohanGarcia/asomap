# Generated manually for changing URLField to FileField

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_financialstatementsconfig_and_more'),
    ]

    operations = [
        # Remover el campo url
        migrations.RemoveField(
            model_name='financialdocument',
            name='url',
        ),
        
        # Agregar el campo file
        migrations.AddField(
            model_name='financialdocument',
            name='file',
            field=models.FileField(
                blank=True,
                help_text='Subir archivo PDF del documento financiero',
                null=True,
                upload_to='financial_documents/',
                verbose_name='Archivo PDF'
            ),
        ),
    ]
