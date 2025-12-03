from django.contrib import admin
from ..models import Gestacion

@admin.register(Gestacion)
class GestacionAdmin(admin.ModelAdmin):
    list_display = ("paciente", "matrona", "fecha_gestacion", "estado_actual")

