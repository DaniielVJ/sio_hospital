from django.db import models

# ESTE MODELO NO TIENE FORMULARIO
class TipoDeIngreso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)


# ESTE MODELO NO TIENE FORMULARIO
class GrupoRobson(models.Model):
    grupo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()


# ESTE MODELO NO TIENE FORMULARIO
class Complicacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()


# ESTE MODELO NO TIENE FORMULARIO
class ViaNacimiento(models.Model):
    tipo = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField()



