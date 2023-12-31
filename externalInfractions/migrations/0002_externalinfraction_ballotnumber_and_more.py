# Generated by Django 4.2.5 on 2023-09-24 02:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("externalInfractions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="externalinfraction",
            name="ballotNumber",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="externalinfraction",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="externalinfraction",
            name="infractionCode",
            field=models.TextField(default="M00"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="externalinfraction",
            name="code",
            field=models.TextField(),
        ),
    ]
