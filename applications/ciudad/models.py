from applications.pais.models import Pais
from django.db import models


class Ciudad(models.Model):
    codigo_posta = models.CharField('Codigo postal', max_length=5, unique=True)
    nombre_ciudad = models.CharField(
        'Nombre ciudad', max_length=20, unique=True)
    descripcion_ciudad = models.CharField('Descripcion ciudad', max_length=50)
    pais = models.ForeignKey(
        Pais, on_delete=models.CASCADE, related_name='ciudades', default=1)

    def __str__(self):
        return f'{self.codigo_posta} - {self.nombre_ciudad} - {self.descripcion_ciudad}'
