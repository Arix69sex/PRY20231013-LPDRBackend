# Generated by Django 4.2.3 on 2023-08-23 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('licensePlates', '0002_rename_hasinfraction_licenseplate_hasinfractions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('licensePlate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licensePlates.licenseplate')),
            ],
        ),
    ]
