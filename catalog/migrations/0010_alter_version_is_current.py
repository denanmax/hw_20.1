# Generated by Django 4.2.4 on 2023-08-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_version_is_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_current',
            field=models.BooleanField(default=False, verbose_name='признак текущаей версии'),
        ),
    ]
