from django.contrib import admin
from ..models import Profesional



@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'tipo',
        'rut',
    )
    list_filter = ('tipo',)
    search_fields = ('nombre', 'rut')