# Generated by Django 5.0.6 on 2024-06-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True, verbose_name='Цена'),
        ),
    ]
