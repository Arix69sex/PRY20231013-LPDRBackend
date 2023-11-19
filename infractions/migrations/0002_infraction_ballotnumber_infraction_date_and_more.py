# Generated by Django 4.2.5 on 2023-09-24 04:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("infractions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="infraction",
            name="ballotNumber",
            field=models.TextField(default="0"),
        ),
        migrations.AddField(
            model_name="infraction",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="infraction",
            name="infractionCode",
            field=models.TextField(default="M00"),
        ),
    ]