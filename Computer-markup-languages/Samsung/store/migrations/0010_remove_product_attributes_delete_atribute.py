# Generated by Django 4.0.4 on 2022-04-24 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_atribute_remove_product_attributes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='attributes',
        ),
        migrations.DeleteModel(
            name='Atribute',
        ),
    ]
