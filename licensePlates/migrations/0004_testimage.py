# Generated by Django 4.2.3 on 2023-09-07 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensePlates', '0003_licenseplate_imagedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
