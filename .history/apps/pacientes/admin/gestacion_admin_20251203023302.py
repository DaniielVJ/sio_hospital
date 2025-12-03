from django.contrib import admin
from ..models import Gestacion

@admin.register(Gestacion)
class GestacionAdmin(admin.ModelAdmin):
    list_display = ("paciente", "matrona", "semana_gestacion", "dias_gestacion", "multiple", "numero_fetos", "riezgo","terminado", "aborto")
    search_fields = ("paciente__nombre", "paciente__apellido_paterno", "paciente_identificacion", "matrona__username")
    list_filter = ("riezgo","multiple","terminado", "aborto", "enfermedad_cardiaca", "hipertension", "diabetes", "fecha_ingreso")

    ordering = ("-fecha_ingreso",)
    list_per_page = 20

    fieldsets = (
        ("Información de Gestación", {
            "fields": (
                ("paciente", "matrona","semana_gestacion","dias_gestacion","multiple", "numero_fetos","riezgo",)
        }),}),
        ("Estado Final", {
            "fields": ("terminado", "aborto",)
        }).


                "fecha_ingreso",
                ("terminado", "aborto"),
                (
                    "enfermedad_cardiaca",
                    "hipertension",
                    "diabetes",
                    "otras_enfermedades",
                ),
            )
        )
    )