from django.contrib import admin

# Register your models here.
from .models import Gestacion, TipoPaciente, Paciente

@admin.register(Gestacion)
class GestacionAdmin(admin.ModelAdmin):
    search_fields = ['paciente__rut']


@admin.register(TipoPaciente)
class TipoPacienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass

