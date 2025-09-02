# Generated manually for FinancialDocument and FinancialStatement updates

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_communityinitiative_image_alt'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=500)),
                ('document_type', models.CharField(choices=[('audited', 'Auditado'), ('quarterly', 'Trimestral')], max_length=10)),
                ('quarter', models.CharField(blank=True, help_text='Solo para documentos trimestrales (1, 2, 3, 4)', max_length=2, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Financial Document',
                'verbose_name_plural': 'Financial Documents',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='title',
            field=models.CharField(default='Estados Financieros', max_length=200),
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='description',
            field=models.TextField(default='Consulta nuestros estados financieros auditados y trimestrales'),
        ),
        migrations.AlterField(
            model_name='financialstatement',
            name='year',
            field=models.CharField(max_length=4),
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='audited_documents',
            field=models.ManyToManyField(blank=True, related_name='audited_statements', to='about.financialdocument'),
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='quarterly_documents',
            field=models.ManyToManyField(blank=True, related_name='quarterly_statements', to='about.financialdocument'),
        ),
    ]
