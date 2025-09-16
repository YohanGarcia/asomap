# Generated manually to fix loan verbose names

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_loan_loan_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loan',
            options={'ordering': ['loan_type', 'title'], 'verbose_name': 'Préstamo', 'verbose_name_plural': 'Préstamos'},
        ),
    ]
