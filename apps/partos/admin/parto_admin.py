from django.contrib import admin
from ..models import Parto

@admin.register(Parto)
class PartoAdmin(admin.ModelAdmin):
    pass
