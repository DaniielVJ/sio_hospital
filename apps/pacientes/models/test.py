from django.db import models
from .gestacion import Gestacion
from ..fields import OrderField

class Test(models.Model):
    class Resultado(models.TextChoices):
        REACTIVO = "positivo", "Reactivo"
        NO_REACTIVO = "negativo", "No Reactivo"
    
    gestacion = models.ForeignKey(Gestacion, on_delete=models.CASCADE, 
                                  related_name="%(class)s")
    resultado = models.CharField(max_length=15,
                                 choices=Resultado.choices,
                                 default=Resultado.NO_REACTIVO)
    fecha_toma = models.DateField()
    durante_parto = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)
    antibiotico = models.BooleanField(default=False)
    orden = OrderField(for_fields=['gestacion'])

    class Meta:
        abstract = True


class TestVih(Test):

    class Trimestre(models.TextChoices):
        PRIMERO = '1', 'Primer Trimestre (0-12 semanas)'
        SEGUNDO = '2', 'Segundo Trimestre (13-27 semanas)'
        TERCERO = '3', 'Tercer Trimestre (28-40 semanas)'

    n_aro = models.IntegerField()
    en_preparto = models.BooleanField(default=False)
    en_sala = models.BooleanField(default=False)
    trimestre = models.CharField(max_length=20, 
                                 choices=Trimestre.choices,
                                 default=Trimestre.PRIMERO)


class TestSgb(Test):
    pass

class TestVdrl(Test):
    pass

class TestHepatitisB(Test):
    derivacion_especialista = models.BooleanField(default=False)

