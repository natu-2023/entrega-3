from django.db import models

# Create your models here.
from django.db import models


class Disfraces(models.Model):
    disfraces = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.disfraces} ({self.precio})"