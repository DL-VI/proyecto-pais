# Generated by Django 5.0.4 on 2024-06-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('continente', '0006_remove_continente_pais'),
        ('pais', '0010_remove_pais_continente'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='continente',
            field=models.ManyToManyField(related_name='paises', to='continente.continente'),
        ),
    ]