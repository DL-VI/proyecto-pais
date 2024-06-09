from django.db import models
from applications.idioma.models import Idioma


class Pais(models.Model):
    codigo_pais = models.CharField('Codigo Pais', max_length=10, unique=True)
    nombre_pais = models.CharField('Nombre Pais', max_length=30, unique=True)
    idioma = models.ManyToManyField(Idioma, related_name='paises')

    def __str__(self) -> str:
        return f'{self.codigo_pais} - {self.nombre_pais}'
