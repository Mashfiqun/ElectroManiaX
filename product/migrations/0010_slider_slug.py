# Generated by Django 5.1 on 2024-09-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_laptop_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slug',
            field=models.SlugField(default=None, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
