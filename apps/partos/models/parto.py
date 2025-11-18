from django.db import models
from django.conf import settings

from .detalle_parto import (Analgesia, Complicacion, 
                            GrupoRobson, TipoDeIngreso,
                            ViaNacimiento)
from .profesional import Profesional
from apps.pacientes.models.gestacion import Gestacion

class Parto(models.Model):

    class TipoRotura(models.TextChoices):
        ESPONTANEA = 'espontanea', "Espontánea"
        ARTIFICIAL = 'artificial', 'Artificial'
    
    class EstadoParto(models.TextChoices):
        TERMINADO = 'terminado', 'Terminado'
        ABORTO = 'aborto', 'Aborto'

    class EstadoPerine(models.TextChoices):
        INDEMNE = 'indemne', 'Indemne'
        DESGARRO_G1 = 'g1', 'Desgarro G1'
        DESGARRO_G2 = 'g2', 'Desgarro G2'
        DESGARRO_G3A = 'g3a', 'Desgarro G3 A'
        DESGARRO_G3B = 'g3b', 'Desgarro G3 B'
        DESGARRO_G3C = 'g3c', 'Desgarro G3 C'
        DESGARRO_G4 = 'g4', 'Desgarro G4'
        FISURA = 'fisura', 'Fisura'
        EPISIOTOMIA ='episiotomia', 'Episiotomia'
    
    class PosicionParto(models.TextChoices):
        SEMISENTADA = 'semisentada', 'Semisentada'
        SENTADA = 'sentada', 'Sentada'
        LITOTOMIA = 'litotomia', 'Litotomia'
        D_DORSAL = 'dorsal', 'D.Dorsal'
        CUADRUPEDA = 'cuadrupeda', 'Cuadrúpeda'
        D_LATERAL = 'lateral', 'D.Lateral'
        DE_PIE = 'de pie', 'De Pie'
        CUCLILLAS = 'cuclillas', 'Cuclillas'
        OTRO = 'otro', 'Otro'

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                related_name='partos')
    tipo_de_ingreso = models.ForeignKey(TipoDeIngreso, on_delete=models.PROTECT, related_name='partos')
    grupo_robson = models.ForeignKey(GrupoRobson, on_delete=models.PROTECT, related_name="partos")
    via_nacimiento = models.ForeignKey(ViaNacimiento, on_delete=models.PROTECT, related_name="partos")
    gestacion = models.OneToOneField(Gestacion, on_delete=models.PROTECT, related_name="parto")
    analgesias = models.ManyToManyField(Analgesia, related_name="partos")
    complicaciones = models.ManyToManyField(Complicacion, related_name="partos")
    profesionales = models.ManyToManyField(Profesional, related_name="partos")
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    numero_aro = models.PositiveSmallIntegerField()
    paridad = models.PositiveSmallIntegerField()
    n_gestaciones = models.PositiveSmallIntegerField()
    n_tactos_vaginales = models.PositiveSmallIntegerField()
    rotura_membrana = models.CharField(max_length=50,
                                       choices=TipoRotura.choices,
                                       default=TipoRotura.ESPONTANEA)
    estado = models.CharField(max_length=30,
                              choices=EstadoParto.choices,
                              default=EstadoParto.TERMINADO)
    estado_perine = models.CharField(max_length=30,
                                     choices=EstadoPerine.choices,
                                     default=EstadoPerine.INDEMNE)
    posicion = models.CharField(max_length=50,
                                choices=PosicionParto.choices,
                                default=PosicionParto.OTRO)
    tiempo_membrana_rota = models.PositiveSmallIntegerField()
    tiempo_dilatacion = models.PositiveSmallIntegerField()
    tiempo_expulsivo = models.PositiveSmallIntegerField()
    edad_madre = models.PositiveSmallIntegerField()
    semana_gestaciones = models.PositiveSmallIntegerField()
    monitor = models.BooleanField(default=False)
    entrega_placenta = models.BooleanField(default=False)
    acompaniante = models.BooleanField(default=False)
    ttc = models.BooleanField(default=False)
    induccion = models.BooleanField(default=False)
    aceleracion = models.BooleanField(default=False)
    oxitocina_profilactica = models.BooleanField(default=False)
    uso_sala_saip = models.BooleanField(default=False)
    esterilizacion = models.BooleanField(default=False)
    


