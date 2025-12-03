from django.db import models
from .rn import RecienNacido
from apps.partos.models import Profesional

class TipoVacuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)



class Vacunacion(models.Model):
    recien_nacido = models.ForeignKey(RecienNacido, on_delete=models.CASCADE, related_name='vacunaciones')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='vacunaciones')
    fecha = models.DateField()
    reaccion_adversa = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoVacuna, on_delete=models.PROTECT, related_name='vacunas')