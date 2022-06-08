from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


TIPOS = [
    ('1','laptop'),
    ('2','cpu'),
    ('3','impresora'),
    ('4',"todo en uno"),
    ('5','otros'),

]

class DatosPersonales(models.Model):
    numero = models.IntegerField('Número')
    nombre = models.CharField("Nombre completo", max_length=100)
    num_serie = models.ForeignKey("cliente.Dispositivo", verbose_name="Número de serie", on_delete=models.CASCADE)

    def __str__(self):
        return self.numero

class Dispositivo(models.Model):
    tipo = models.CharField("Tipo", max_length=1,choices=TIPOS)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100)
    accesorios = models.CharField("Accesorios", max_length=200)
    contra = models.CharField("Contraseña", max_length=100)
    falla = models.CharField("Fallas", max_length=100)
    extras = models.CharField("Extras", max_length=100)

    def __str__(self):
        return self.num_serie