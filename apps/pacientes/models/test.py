from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from .gestacion import Gestacion
from ..fields import OrderField

class Test(models.Model):
    
    class Resultado(models.TextChoices):
        REACTIVO = "positivo", "Reactivo"
        NO_REACTIVO = "negativo", "No Reactivo"
    
    class LugarToma(models.TextChoices):
        PREPARTO = 'preparto', 'Preparto'
        SALA_PARTO = 'sala_parto', 'Sala de Partos'
        URGENCIA = 'urgencia', 'Urgencias'
            
    
    gestacion = models.ForeignKey(Gestacion, on_delete=models.CASCADE, 
                                  related_name="%(class)s")
    resultado = models.CharField(max_length=15,
                                 choices=Resultado.choices,
                                 default=Resultado.NO_REACTIVO)
    fecha_toma = models.DateField(help_text="Fecha en la que se tomo el examen")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    lugar_toma = models.CharField(max_length=12,
                                  choices=LugarToma.choices,
                                  default=LugarToma.PREPARTO)
    antibiotico = models.BooleanField(default=False)
    durante_parto = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, max_length=1000)

    orden = OrderField(for_fields=['gestacion'])


    class Meta:
        abstract = True


class TestVih(Test):
    class Trimestre(models.TextChoices):
        PRIMERO = '1', 'Primer Trimestre (0-12 semanas)'
        SEGUNDO = '2', 'Segundo Trimestre (13-27 semanas)'
        TERCERO = '3', 'Tercer Trimestre (28-40 semanas)'


    n_aro = models.PositiveIntegerField()
    trimestre = models.CharField(max_length=20, 
                                 choices=Trimestre.choices,
                                 default=Trimestre.PRIMERO)




class TestSgb(Test):
    pass



class TestVdrl(Test):
    pass

class TestHepatitisB(Test):
    derivacion_especialista = models.BooleanField(default=False)

'''
VALIDACIONES FUNDAMENTALES PARA TESTS DE LABORATORIO (SIN LÓGICA DE NEGOCIO)

Generales (aplican a todos los exámenes)
---------------------------------------
1. Fecha de toma no puede ser futura.
2. Fecha de toma no puede ser anterior al inicio de la gestación (FUR).
3. Validar que el orden es único por gestación (evitar duplicados).
4. Evitar registros duplicados del mismo examen en la misma fecha.
5. Observaciones es opcional, pero validar longitud máxima (ej: 500 caracteres).
6. Nunca modificar fecha_registro (auto_now_add=true).

Test VIH
--------
7. Validar que el trimestre esté dentro de los choices establecidos.
8. Validar que n_aro sea un número positivo.

Test SGB, VDRL, Hepatitis B
---------------------------
9. Sin validaciones extra: solo aplicar las generales.

Notas
-----
- No incluir lógica clínica (derivaciones, tratamientos, relaciones entre campos).
- Validar solo integridad técnica y coherencia básica de los datos.

'''