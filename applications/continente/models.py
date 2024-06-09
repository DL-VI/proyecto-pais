from django.db import models
from applications.pais.models import Pais


class Continente(models.Model):
    nombre_continente = models.CharField(
        'Nombre continente', max_length=20, unique=True)
    descripcion_continente = models.CharField(
        'Descripcion continente', max_length=50, unique=True)
    pais = models.ManyToManyField(Pais, related_name='continentes')

    def __str__(self):
        return f'{self.nombre_continente} - {self.descripcion_continente}'
