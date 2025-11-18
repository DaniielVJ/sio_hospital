from django.db import models

class TipoDeIngreso(models.Model):
    nombre = models.CharField(max_length=50)


class GrupoRobson(models.Model):
    grupo = models.CharField(max_length=50)
    descripcion = models.TextField()


class Complicacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


class ViaNacimiento(models.Model):
    tipo = models.CharField(max_length=60)
    descripcion = models.TextField()

class Analgesia(models.Model):
    tipo = models.CharField(max_length=45)
    descripcion = models.TextField()
