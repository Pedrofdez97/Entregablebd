
from django.db import models

class Equipo(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.TextField()
    campo = models.TextField()
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.nombre