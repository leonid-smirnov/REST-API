# Generated by Django 3.2.8 on 2021-12-21 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito_parser', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]