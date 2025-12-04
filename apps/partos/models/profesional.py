from django.db import models


class Profesional(models.Model):
    class Tipo(models.TextChoices):
        ALUMNO = 'alumno', 'Alumno'
        PROFESOR = 'profesor', 'Profesor'
        ENFERMERA = 'enfermera', 'Enfermera'
        AYUDANTE = 'ayudante', 'Ayudante'
        MATRONA = 'matrona', 'Matrona'
        MEDICO = 'medico', 'Medico Obstetra'
        ANESTESIOLOGO = 'anestesiologo', 'Anestesiologo'
        PEDIATRA = 'pediatra', 'Pediatra o Neonatólogo'
    nombre = models.CharField(max_length=45)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45)
    rut = models.CharField(max_length=11, unique=True)
    tipo = models.CharField(max_length=30,
                            choices=Tipo.choices,
                            default=Tipo.ENFERMERA)
    telefono = models.CharField(max_length=45)
    correo = models.CharField(max_length=60)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido} {self.segundo_apellido} ({self.get_tipo_display()})"
