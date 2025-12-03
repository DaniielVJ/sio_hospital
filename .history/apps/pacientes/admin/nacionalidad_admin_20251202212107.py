from django.contrib import admin
from ..models import Nacionalidad

@admin.register(Nacionalidad)
class nacionalidadAdmin(admin.ModelsAdmin)