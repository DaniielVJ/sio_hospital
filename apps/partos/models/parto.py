from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator


from .detalle_parto import (Complicacion, 
                            GrupoRobson, TipoDeIngreso,
                            ViaNacimiento)
from apps.pacientes.models.gestacion import Gestacion


# Datos ingresados durante el trabajo de parto o parto
class Parto(models.Model):

# Esto no respeta la normalizacion de DB, pero en otra version se les hace un modelo
# a cada una
   class TipoRotura(models.TextChoices):
      ESPONTANEA = 'espontanea', "Espontánea"
      ARTIFICIAL = 'artificial', 'Artificial'
    

   class TipoRegimen(models.TextChoices):
      CERO = 'cero', 'Cero'
      LIQUIDO = 'liquido', 'Liquido'
      COMUN =  'comun', 'Comun'
      OTRO = 'otro', 'Otro'


   class EstadoParto(models.TextChoices):
      CERRADO = 'terminado', 'Terminado'
      INGRESO = 'ingreso', 'Ingreso'
      ACTIVO = 'activo', 'Activo'
      EXPULSIVO = 'expulsivo', 'Expulsivo'
      ALUMBRAMIENTO = 'alumbramiento', 'Alumbramiento'
      PUERPERIO = 'puerperio', 'Puerperio Inmediato'

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

   # NO VAN EN EL FORMULARIO
   created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                              related_name='partos', null=True)
   created_at = models.DateTimeField(auto_now_add=True)

   updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, 
                                 related_name='partos_actualizados', null=True)
   updated_at = models.DateTimeField(auto_now=True)


   tipo_de_ingreso = models.ForeignKey(TipoDeIngreso, on_delete=models.PROTECT, related_name='partos')
   grupo_robson = models.ForeignKey(GrupoRobson, on_delete=models.PROTECT, related_name="partos", blank=True, null=True)
   via_nacimiento = models.ForeignKey(ViaNacimiento, on_delete=models.PROTECT, related_name="partos")
   gestacion = models.OneToOneField(Gestacion, on_delete=models.PROTECT, related_name="parto")
   complicaciones = models.ManyToManyField(Complicacion, related_name="partos")
   hora_inicio = models.DateTimeField()
   numero_aro = models.PositiveSmallIntegerField(default=0)
   
   n_tactos_vaginales = models.PositiveSmallIntegerField(validators=[MaxValueValidator(40)], default=0)
   
   rotura_membrana = models.CharField(max_length=50,
                                    choices=TipoRotura.choices,
                                    default=TipoRotura.ESPONTANEA)
   estado = models.CharField(max_length=30,
                           choices=EstadoParto.choices,
                           default=EstadoParto.INGRESO)

   posicion = models.CharField(max_length=50,
                              choices=PosicionParto.choices,
                              default=PosicionParto.OTRO)
   tipo_regimen = models.CharField(max_length=50,
                                   choices=TipoRegimen.choices,
                                   default=TipoRegimen.CERO)

   observaciones = models.TextField(blank=True, max_length=1000)

   # Acordarse que estos campos deben guardarse con timedelta y en minutos
   tiempo_membrana_rota = models.DurationField()
   tiempo_dilatacion = models.DurationField()
   tiempo_expulsivo = models.DurationField()
   # NO VA EN EL FORMULARIO
   edad_madre = models.PositiveSmallIntegerField()
   monitor = models.BooleanField(default=False)
   entrega_placenta = models.BooleanField(default=False)
   acompaniante = models.BooleanField(default=False)
   ttc = models.BooleanField(default=False)
   induccion = models.BooleanField(default=False)
   aceleracion = models.BooleanField(default=False)
   oxitocina_profilactica = models.BooleanField(default=False)
   uso_sala_saip = models.BooleanField(default=False)
   
   def __str__(self):
      return f"Parto de gestación {self.gestacion.pk}"


   def save(self, *args, **kwargs):
      if not self.edad_madre:
         self.edad_madre = self.gestacion.paciente.calcular_edad_paciente()
      super().save(*args, **kwargs)



'''
10. Integridad de FK/M2M
   - Validar que las instancias de tipo_de_ingreso, robson, via_nacimiento, profesionales existan.
'''