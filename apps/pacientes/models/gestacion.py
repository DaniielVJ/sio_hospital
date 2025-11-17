from django.db import models
from django.conf import settings
from .paciente import Paciente
from ..fields import OrderField

class Gestacion(models.Model):
    class Riesgo(models.TextChoices):
        BAJO = "BAJO", "Bajo Riesgo"
        MEDIO = "MEDIO", "Riesgo Moderado"
        ALTO = "ALTO", "Alto Riesgo"

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="gestaciones")
    # Solo se deben asociar los usuarios que sean matronas (es_matrona = True)
    matrona = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="gestaciones")
    semana_gestacion = models.PositiveSmallIntegerField()
    dias_gestacion = models.PositiveSmallIntegerField()
    hipertension = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    enfermedad_cardiaca = models.BooleanField(default=False)
    multiple = models.BooleanField(default=False)
    numero_fetos = models.PositiveSmallIntegerField()
    terminado = models.BooleanField(default=False)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    # Este campo se encargara de mostrar al matron cuando fue la ultima visita
    # del paciente que actualizo los datos de su gestación en base a los examenes y controles
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    riezgo = models.CharField(max_length=10, 
                              choices=Riesgo.choices,
                              default=Riesgo.BAJO)
    numero_gestacion = OrderField(for_fields=['paciente'])