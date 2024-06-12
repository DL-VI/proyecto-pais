from django.db import models


class Idioma(models.Model):
    codigo_idioma = models.CharField(
        'Codigo Idioma', max_length=10)
    nombre_idioma = models.CharField(
        'Nombre Idioma', max_length=15, unique=True)

    def __str__(self) -> str:
        return f'{self.codigo_idioma} - {self.nombre_idiomaa}'
