from django.contrib import admin
from ..models.rn import RecienNacido

@admin.register(RecienNacido)
class RecienNacidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre_completo', 'fecha_hora', 'peso', 'talla', 'parto', 'presentacion_fetal', 'destino_rn',)
    search_fields = ('codigo', 'nombre_completo', 'parto__codigo_parto', 'presentacion_fetal__nombre',)
    list_filter = ( 'presentacion_fetal', 'destino_rn', 'fecha_hora', 'alojamiento_conjunto', 'apego_canguro','lactante_60','apego_tunel', 'gases_de_cordon',)
    filter_horizontal = ('complicaciones_post_parto', 'reanimacion_neonatal',)
    ordering = ('-fecha_hora',)
    list_per_page = 20
    

    fieldsets = (
        ('Identificación RN',{

        })
    ), 
    pass   



    (
        ('Medidas Antropométricas',{

        })
    ), 
    pass    

    (
        ('Apgar',{

        })
    ), 
    pass    

    (
        ('Presentación y Reanimación',{

        })
    ), 
    pass    

    (
        ('Cuidados y obeservaciones',{

        })
    ), 
    pass    