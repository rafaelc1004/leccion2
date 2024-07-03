import datetime
from typing import Any
from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=False)
    comentario = models.TextField(max_length=1000)
    fechaPublicacion = models.DateField(auto_now_add=True, blank=True)