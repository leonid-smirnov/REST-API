# Generated by Django 3.2.8 on 2022-01-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito_parser', '0009_remove_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на объявление'),
        ),
    ]
