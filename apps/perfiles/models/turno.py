from django.db import models


# El supervisor crea turnos y se lo asocia a la matrona
class Turno(models.Model):
    tipo = models.CharField(max_length=30, choices=[("diurno", "Diurno"), ("vespertino", "Vespertino")])
    nombre = models.CharField(max_length=30)
    hora_ingreso = models.TimeField()
    hora_egreso = models.TimeField()


    def __str__(self):
        return f"Turno: {self.nombre} / {self.tipo}"


