# Generated by Django 5.1 on 2024-09-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_casing_cpucooler_graphicscard_harddisk_keyboards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpucooler',
            name='fan_speed',
            field=models.IntegerField(),
        ),
    ]
