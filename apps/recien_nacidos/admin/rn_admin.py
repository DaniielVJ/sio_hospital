from django.contrib import admin
from ..models.rn import RecienNacido

@admin.register(RecienNacido)
class RecienNacidoAdmin(admin.modelAdmin):
    list_display = ("codigo", "nombre_completo", "fecha_hora", "peso", "talla", "parto", "presentacion_fetal", "destino_rn",)
    search_fields = ("codigo", "nombre_completo", "parto__codigo_parto", "presentacion_fetal__nombre",)
    list_filter = ( "presentacion_fetal", "destino_rn", "fecha_hora", "alojamiento_conjunto", "apego_canguro",)

