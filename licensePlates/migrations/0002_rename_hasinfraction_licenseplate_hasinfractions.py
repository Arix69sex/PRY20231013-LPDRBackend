# Generated by Django 4.2.3 on 2023-08-22 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licensePlates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licenseplate',
            old_name='hasInfraction',
            new_name='hasInfractions',
        ),
    ]
