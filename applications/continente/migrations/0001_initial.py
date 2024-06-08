# Generated by Django 5.0.4 on 2024-06-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_continente', models.CharField(max_length=20, unique=True, verbose_name='Nombre continente')),
                ('descripcion_continente', models.CharField(max_length=50, unique=True, verbose_name='Descripcion continente')),
            ],
        ),
    ]
