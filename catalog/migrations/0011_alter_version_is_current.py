# Generated by Django 4.2.4 on 2023-08-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_product_is_active_alter_version_is_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_current',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='признак текущей версии'),
        ),
    ]
