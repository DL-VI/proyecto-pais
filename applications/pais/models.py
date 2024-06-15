from django.db import models
from applications.continente.models import Continente
from applications.idioma.models import Idioma


class Pais(models.Model):
    """
    Representa un país.

    Atributos:
        codigo_pais (str): El código del país.
        nombre_pais (str): El nombre del país.
        idioma (ManyToManyField): Los idiomas hablados en el país.
        continente (ManyToManyField): Los continentes a los que pertenece el país.
    """
    codigo_pais = models.CharField('Codigo Pais', max_length=10, unique=True)
    nombre_pais = models.CharField('Nombre Pais', max_length=30, unique=True)
    idioma = models.ManyToManyField(Idioma, related_name='paises')
    continente = models.ManyToManyField(Continente, related_name='paises')

    def __str__(self):
        return f'{self.codigo_pais} - {self.nombre_pais}'
