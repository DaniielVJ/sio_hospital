from django.db import models
from .detalle_rn import (ComplicacionPostParto, PresentacionFetal, ReanimacionNeonatal)
from apps.partos.models import Parto

class RecienNacido(models.Model):
    # ForeignKey ya que asi podemos asociar uno o mas bebes al mismo parto o diferentes partos, ya que de 1 parto pueden haber mas de 1
    # bebe asociado porque el parto pudo ser multiple
    parto = models.ForeignKey(Parto, on_delete=models.PROTECT, related_name='rns')
    presentacion_fetal = models.ForeignKey(PresentacionFetal, on_delete=models.PROTECT, related_name='rns')
    complicaciones_postparto = models.ManyToManyField(ComplicacionPostParto, related_name='rns')
    reanimaciones_neonatales = models.ManyToManyField(ReanimacionNeonatal, related_name='rns')
    fecha_hora = models.DateTimeField()
    nombre_completo = models.CharField(max_length=150, blank=True)
    peso = models.FloatField()
    talla = models.FloatField()
    apgar_1 = models.PositiveSmallIntegerField()
    apgar_5 = models.PositiveSmallIntegerField()
    codigo = models.CharField(max_length=20)
    perimetro_cefalico = models.FloatField()
    perimetro_toraxico = models.FloatField()
    c_2480 = models.PositiveSmallIntegerField()
    destino_rn = models.CharField(max_length=40)
    alojamiento_conjunto = models.BooleanField()
    observaciones = models.TextField()
    apego_canguro = models.BooleanField()
    lactante_60 = models.BooleanField()
    apego_tunel = models.BooleanField()
    gases_de_cordon = models.BooleanField()