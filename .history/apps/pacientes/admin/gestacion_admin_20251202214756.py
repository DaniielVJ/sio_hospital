from django.contrib import admin
from ..models import Gestacion

@admin.register(Gestacion)
class GestacionAdmin(admin.ModelAdmin):
    list_display = ("paciente", "matrona", "semanas_gestacion", "dias_gestacion", "multiple", "numero_fetos", "riezgo", "fecha_ingreso", "terminado", "aborto")
    search_fields = ("paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno", "matrona__nombre", "matrona__apellido_paterno", "matrona__apellido_materno")

