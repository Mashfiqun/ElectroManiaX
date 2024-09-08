# Generated by Django 5.1 on 2024-09-02 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_delete_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('processor', models.CharField(max_length=250, unique=True)),
                ('display_size', models.DecimalField(decimal_places=1, max_digits=3)),
                ('display_type', models.CharField(max_length=250)),
                ('ram_size', models.CharField(max_length=250)),
                ('ram_type', models.CharField(max_length=250)),
                ('bus_speed', models.CharField(max_length=250)),
                ('storage_size', models.CharField(max_length=250)),
                ('storage_type', models.CharField(max_length=250)),
                ('graphics_size', models.CharField(max_length=250)),
                ('graphics_type', models.CharField(max_length=250)),
                ('keyboard', models.CharField(max_length=250)),
                ('camera', models.CharField(max_length=250)),
                ('speaker', models.BooleanField(default=True)),
                ('mic', models.BooleanField(default=True)),
                ('wifi', models.CharField(max_length=250)),
                ('battery', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=250)),
            ],
            bases=('product.product',),
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_date',
        ),
    ]
