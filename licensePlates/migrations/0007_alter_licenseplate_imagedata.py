# Generated by Django 4.2.5 on 2023-09-21 02:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("licensePlates", "0006_alter_licenseplate_imagedata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="licenseplate",
            name="imageData",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
