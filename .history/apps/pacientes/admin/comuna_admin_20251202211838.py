from django.contrib import admin
from ..models import Comuna

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin)