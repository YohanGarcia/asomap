# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_communitycategory_alter_communitysupport_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityinitiative',
            name='image_alt',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Texto alternativo de imagen'),
        ),
    ]
