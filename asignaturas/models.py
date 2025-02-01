from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100, blank=True, null=True)
    notas_adicionales = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
