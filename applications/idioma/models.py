from django.db import models
from applications.pais.models import Pais


class Idioma(models.Model):
    codigoIdioma = models.CharField(
        'Codigo Idioma', max_length=10, unique=True)
    nombreIdioma = models.CharField(
        'Nombre Idioma', max_length=15, unique=True)
    idioma_pais = models.ForeignKey(Pais, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.codigoIdioma + ' - ' + self.idioma_pais
