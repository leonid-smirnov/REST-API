# Generated by Django 3.2.8 on 2022-01-10 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avito_parser', '0008_auto_20220110_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='currency',
        ),
    ]