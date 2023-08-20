# Generated by Django 4.2.3 on 2023-08-20 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_user_createdat_delete_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.TextField()),
                ('names', models.CharField(max_length=50)),
                ('lastNames', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
