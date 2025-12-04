from django.db import models

class TipoDeIngreso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)


class GrupoRobson(models.Model):
    grupo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()


class Complicacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()


class ViaNacimiento(models.Model):
    tipo = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField()



