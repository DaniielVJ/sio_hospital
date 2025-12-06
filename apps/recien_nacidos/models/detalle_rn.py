from django.db import models


# NO POSEE FORMULARIO NINGUNO DE ESTOS MODELOS
class ComplicacionPostParto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


class PresentacionFetal(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


class ReanimacionNeonatal(models.Model):
    class TipoReanimacion(models.TextChoices):
        BASICA = ('basica', 'Básica')
        AVANZADA = ('avanzada', 'Avanzada')
    
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=15,
                            choices=TipoReanimacion.choices,
                            default=TipoReanimacion.BASICA)
