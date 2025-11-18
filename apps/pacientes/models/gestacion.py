from django.db import models
from django.conf import settings
from .paciente import Paciente
from ..fields import OrderField

class Gestacion(models.Model):
    class Riesgo(models.TextChoices):
        BAJO = "BAJO", "Bajo Riesgo"
        MEDIO = "MEDIO", "Riesgo Moderado"
        ALTO = "ALTO", "Alto Riesgo"

    class Estado(models.TextChoices):
        TERMINADA = 'terminada', 'Terminada'
        ABORTO = 'aborto', 'Aborto'

    paciente = models.ForeignKey(Paciente, 
                                 on_delete=models.CASCADE, 
                                 related_name="gestaciones")
    # Solo se deben asociar los usuarios que sean matronas (es_matrona = True)
    matrona = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="gestaciones")
    semana_gestacion = models.PositiveSmallIntegerField()
    dias_gestacion = models.PositiveSmallIntegerField()
    multiple = models.BooleanField(default=False)
    numero_fetos = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    # Este campo se encargara de mostrar al matron cuando fue la ultima visita
    # del paciente que actualizo los datos de su gestación en base a los examenes y controles
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    riezgo = models.CharField(max_length=10, 
                              choices=Riesgo.choices,
                              default=Riesgo.BAJO)
    numero_gestacion = OrderField(for_fields=['paciente'])

    # PARA EL CHAMO
    # ESTADO DEL PARTO: Marque estas opciones si la gestación finalizo o termino en aborto, si no no marque nada
    terminado = models.BooleanField(default=False)
    aborto = models.BooleanField(default=False)
    # COMPLICACIONES: Marque todas las complicaciones o riesgo que posee esta gestación para el parto
    enfermedad_cardiaca = models.BooleanField(default=False)
    hipertension = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    