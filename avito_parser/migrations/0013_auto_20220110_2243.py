# Generated by Django 3.2.8 on 2022-01-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito_parser', '0012_alter_product_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='floor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='Ссылка на объявление'),
        ),
    ]
