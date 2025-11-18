from django.db import models

class TipoPaciente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)


class Paciente(models.Model):

    class Actividad(models.TextChoices):
        BAJA = 'baja', 'Baja'
        MODERADA = 'moderada', 'Moderada'
        ALTA = 'alta', 'Alta'

    # fonasa, isapre, etc.
    tipo = models.ForeignKey(TipoPaciente, on_delete=models.PROTECT, related_name="paciente")
    nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    nacionalidad = models.CharField(max_length=100)
    comuna = models.CharField(max_length=59)
    cesfam = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField()
    es_descapacitado = models.BooleanField(default=False)
    es_pueblo_originario = models.BooleanField(default=False)
    es_privada_de_libertad = models.BooleanField(default=False)
    es_transexual = models.BooleanField(default=False)
    plan_de_parto = models.BooleanField(default=False)
    visita_guiada = models.BooleanField(default=False)
    peso = models.FloatField()
    altura = models.FloatField()
    actividad = models.CharField(max_length=9,
                                 choices=Actividad.choices,
                                 default=Actividad.BAJA)

    def __str__(self):
        return super().__str__()
    

    def calcular_Imc(self):
        pass
    

