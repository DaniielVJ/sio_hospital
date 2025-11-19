from django.db import models
from .rn import RecienNacido
from apps.partos.models import Profesional


class Vacunacion(models.Model):
    recien_nacido = models.ForeignKey(RecienNacido, on_delete=models.CASCADE, related_name='vacunaciones')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='vacunaciones')
    fecha = models.DateField()
    reaccion_adversa = models.CharField(max_length=100)
    