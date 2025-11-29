# Register your models here.
from django.contrib import admin
from ..models import Parto


@admin.register(Parto)
class PartoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'gestacion',
        'usuario',
        'via_nacimiento',
        'estado',
        'fecha_ingreso',
    )

    # ACORDARSE QUE ESTE CAMPO DEPENDE DEL SEARCH_FIELD DEL OTRO MODELO SI APUNTA AL OTRO MODELO
    # EN ESTE CASO PERMITE AUTOCOMPLETADO EN GESTACION Y BUSCAR POR RUT PACIENTE
    autocomplete_fields = ('gestacion', )
    
    list_filter = (
        'via_nacimiento',
        'estado',
        'tipo_de_ingreso',
        'grupo_robson',
        'profesionales',
        'analgesias',
        'complicaciones',
    )

    search_fields = (
        'gestacion__paciente__rut',  
        'usuario__username',
        'usuario__perfilmatrona__rut'
    )

    filter_horizontal = (
        'analgesias',
        'complicaciones',
        'profesionales',
    )

    fieldsets = (
        ('Información general', {
            'fields': (
                'usuario',
                'gestacion',
                # 'fecha_ingreso',
                'estado',
            )
        }),

        ('Datos obstétricos', {
            'fields': (
                'tipo_de_ingreso',
                'grupo_robson',
                'via_nacimiento',
                'posicion',
                'estado_perine',
                'rotura_membrana',
                'tiempo_membrana_rota',
                'tiempo_dilatacion',
                'tiempo_expulsivo',
                'numero_aro',
                'paridad',
                'n_gestaciones',
                'n_tactos_vaginales',
                'edad_madre',
                'semanas_gestacionales',
            )
        }),

        ('Acciones y procesos', {
            'fields': (
                'induccion',
                'aceleracion',
                'oxitocina_profilactica',
                'entrega_placenta',
                'esterilizacion',
                'monitor',
                'uso_sala_saip',
                'acompaniante',
                'ttc',
            )
        }),

        ('Analgesias y complicaciones', {
            'fields': (
                'analgesias',
                'complicaciones',
            )
        }),

        ('Profesionales presentes', {
            'fields': ('profesionales',)
        }),
    )



