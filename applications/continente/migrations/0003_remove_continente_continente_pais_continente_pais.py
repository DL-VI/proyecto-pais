# Generated by Django 5.0.4 on 2024-06-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continente', '0002_continente_continente_pais'),
        ('pais', '0007_pais_pais_ciudad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='continente',
            name='continente_pais',
        ),
        migrations.AddField(
            model_name='continente',
            name='pais',
            field=models.ManyToManyField(related_name='continentes', to='pais.pais'),
        ),
    ]