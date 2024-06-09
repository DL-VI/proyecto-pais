# Generated by Django 5.0.4 on 2024-06-09 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudad', '0003_initial'),
        ('pais', '0007_pais_pais_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ciudades', to='pais.pais'),
        ),
    ]