# Generated by Django 4.1 on 2022-12-12 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_rename_asset_asset_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeasset',
            old_name='asset',
            new_name='name',
        ),
    ]
