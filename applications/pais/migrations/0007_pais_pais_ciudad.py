# Generated by Django 5.0.4 on 2024-06-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudad', '0003_initial'),
        ('pais', '0006_remove_pais_pais_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='pais_ciudad',
            field=models.ManyToManyField(to='ciudad.ciudad'),
        ),
    ]
