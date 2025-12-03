from django.contrib import admin
from ..

@admin.register(Cesfam)
class CesfamAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "comuna")
    search_fields = ("nombre", "comuna__nombre")
    list_filter = ("comuna",)
    ordering = ("nombre",)  
