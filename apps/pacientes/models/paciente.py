from django.db import models

class TipoPaciente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Cesfam(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)

    class Meta:
        ordering = ['comuna__nombre', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.comuna})"


class Paciente(models.Model):

    class Actividad(models.TextChoices):
        BAJA = 'baja', 'Baja'
        MODERADA = 'moderada', 'Moderada'
        ALTA = 'alta', 'Alta'

    class TipoDocumento(models.TextChoices):
        RUT = 'RUT', 'Rut'
        PAS = 'PAS', 'Pasaporte'
        EXT = 'EXT', 'Documento extranjero'
        TMP = 'TMP', 'Sin documento / Temporal'  

    # fonasa, isapre, etc.
    tipo = models.ForeignKey(TipoPaciente, on_delete=models.PROTECT, related_name='paciente')
    
    # Puede quedar null ese valor ya que el cesfam comuna o nacionalidad de ese paciente puede desaparecer 
    # y si desaparece simplemente se queda sin esa info pero no deberia desaparecer el paciente
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, related_name='paciente', null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, related_name='paciente', null=True)
    cesfam = models.ForeignKey(Cesfam, on_delete=models.SET_NULL, related_name='paciente', null=True)

    nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)
    
    # Info Documento
    documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.RUT)
    identificacion = models.CharField(max_length=15, unique=True)
    
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
        return f'{self.documento}: {self.identificacion} | paciente: {self.obtener_nombre_completo()}'
    

    def obtener_nombre_completo(self):
        return f'{self.nombre} {self.primer_apellido} {self.segundo_apellido}'

    def calcular_Imc(self):
        pass
    

