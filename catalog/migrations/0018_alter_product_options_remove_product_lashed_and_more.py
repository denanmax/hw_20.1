# Generated by Django 4.2.4 on 2023-08-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_merge_20230830_1006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('set_published_status', 'Can publish post')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='lashed',
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='опубликован'),
        ),
    ]