from django.db import models
from django.conf import settings

from .detalle_parto import (Complicacion, 
                            GrupoRobson, TipoDeIngreso,
                            ViaNacimiento)
from .profesional import Profesional
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

   created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                              related_name='partos', null=True)
   created_at = models.DateTimeField(auto_now_add=True)

   updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, 
                                 related_name='partos_actualizados', null=True)
   updated_at = models.DateTimeField(auto_now=True)


   tipo_de_ingreso = models.ForeignKey(TipoDeIngreso, on_delete=models.PROTECT, related_name='partos')
   grupo_robson = models.ForeignKey(GrupoRobson, on_delete=models.PROTECT, related_name="partos", blank=True)
   via_nacimiento = models.ForeignKey(ViaNacimiento, on_delete=models.PROTECT, related_name="partos")
   gestacion = models.OneToOneField(Gestacion, on_delete=models.PROTECT, related_name="parto")
   complicaciones = models.ManyToManyField(Complicacion, related_name="partos")
   profesionales = models.ManyToManyField(Profesional, related_name="partos")
   hora_inicio = models.DateTimeField()
   numero_aro = models.PositiveSmallIntegerField()
   
   n_tactos_vaginales = models.PositiveSmallIntegerField()
   
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




'''
VALIDACIONES FUNDAMENTALES PARA EL MODELO PARTO
(Sin lógica clínica, solo integridad de datos)

1. Gestación
   - Verificar que la gestación no tenga otro parto (OneToOne).
   - No permitir registrar dos partos para la misma gestación.

2. Edad de la madre
   - Debe ser un número entre 10 y 60 años.

3. Coherencia de tiempos
   - tiempo_membrana_rota >= 0
   - tiempo_dilatacion >= 0
   - tiempo_expulsivo >= 0
   - Valores no negativos. (Opcional: establecer máximos razonables para evitar errores.)

4. Número de tactos vaginales
   - Debe ser >= 0.
   - (Opcional) Máximo razonable, ej. 40, para evitar datos erróneos por tipeo.

5. Coherencia paridad / gestaciones
   - paridad <= n_gestaciones.

6. Número de aro
   - Debe ser >= 1.

7. Profesionales
   - Validar que al menos un profesional esté seleccionado.

8. Campos con choices (via_nacimiento, rotura, estado_perine, etc.)
   - Valores deben corresponder a choices definidos.
   - Django ya valida esto automáticamente.

9. Fecha de ingreso
   - No modificable manualmente (auto_now_add).
   - Validar en el formulario que no se inyecten fechas externas.

10. Integridad de FK/M2M
   - Validar que las instancias de tipo_de_ingreso, robson, via_nacimiento, profesionales existan.

'''