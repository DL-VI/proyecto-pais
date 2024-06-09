from django.db import models
from applications.idioma.models import Idioma
from applications.ciudad.models import Ciudad

# Create your models here.


class Pais(models.Model):
    codigoPais = models.CharField('Codigo Pais', max_length=10, unique=True)
    nombrePais = models.CharField('Nombre Pais', max_length=30, unique=True)
    pais_idioma = models.ManyToManyField(Idioma)
    pais_ciudad = models.ManyToManyField(Ciudad)

    def __str__(self) -> str:
        return f'{self.codigoPais} - {self.nombrePais}'
