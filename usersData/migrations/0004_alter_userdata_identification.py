# Generated by Django 4.2.5 on 2023-09-24 04:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usersData", "0003_alter_userdata_identification"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdata",
            name="identification",
            field=models.TextField(unique=True),
        ),
    ]
