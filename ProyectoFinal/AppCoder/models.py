
from django.db import models


class Disfraces(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField(max_length=10)
    def __str__(self):
        return f"{self.nombre} ({self.precio})"

class TipoDisfraces(models.Model):
    clase = models.CharField(max_length=30)
    talle = models.IntegerField(max_length=10)
    def __str__(self):
        return f"{self.clase} ({self.talle})"

class STock(models.Model):
    clase = models.CharField(max_length=30)
    cantidad = models.IntegerField(max_length=10)
    def __str__(self):
        return f"{self.clase} ({self.cantidad})"