from django.contrib import admin
from ..models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass