from django.contrib import admin
from ..models.rn import RecienNacido

@admin.register(RecienNacido)
class RecienNacidoAdmin(admin.modelAdmin):

