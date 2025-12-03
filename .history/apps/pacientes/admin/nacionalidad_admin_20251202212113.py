from django.contrib import admin
from ..models import Nacionalidad

@admin.register(Nacionalidad)
class nacionalidadAdmin(admin.ModelsAdmin):
    list_display = ("nombre", "codigo_iso")
    search_fields = ("nombre", "codigo_iso")
    ordering = ("nombre",)