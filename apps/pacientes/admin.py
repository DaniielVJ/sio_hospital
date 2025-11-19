from django.contrib import admin

# Register your models here.
from .models import Gestacion

@admin.register(Gestacion)
class GestacionAdmin(admin.ModelAdmin):
    search_fields = ['paciente__rut']