# Generated by Django 4.1 on 2022-12-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_asset_date_entered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date_entered',
            field=models.DateField(null=True),
        ),
    ]
