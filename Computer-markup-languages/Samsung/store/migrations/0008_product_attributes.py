# Generated by Django 4.0.4 on 2022-04-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_category_options_rename_name_category_name_c'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
