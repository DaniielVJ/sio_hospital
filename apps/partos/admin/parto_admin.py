from django.contrib import admin
from ..models import Parto

@admin.register(Parto)
class PartoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'gestacion',
        'created_by',           # antes 'usuario'
        'via_nacimiento',
        'estado',
        'created_at',           # antes 'fecha_ingreso'
    )

    autocomplete_fields = ('gestacion', )
    
    list_filter = (
        'via_nacimiento',
        'estado',
        'tipo_de_ingreso',
        'grupo_robson',
        'profesionales',
        'complicaciones',
    )

    search_fields = (
        'gestacion__paciente__identificacion',  # cambie 'rut' por tu campo 'identificacion'
        'create_by__username',
    )

    filter_horizontal = (
        'profesionales',
        'complicaciones',
    )

    fieldsets = (
        ('Información general', {
            'fields': (
                'create_by',
                'gestacion',
                'estado',
            )
        }),
        ('Datos obstétricos', {
            'fields': (
                'tipo_de_ingreso',
                'grupo_robson',
                'via_nacimiento',
                'posicion',
                'rotura_membrana',
                'tiempo_membrana_rota',
                'tiempo_dilatacion',
                'tiempo_expulsivo',
                'numero_aro',
                'edad_madre',
            )
        }),
        ('Acciones y procesos', {
            'fields': (
                'induccion',
                'aceleracion',
                'oxitocina_profilactica',
                'entrega_placenta',
                'monitor',
                'uso_sala_saip',
                'acompaniante',
                'ttc',
            )
        }),
        ('Analgesias y complicaciones', {
            'fields': (
                'complicaciones',
            )
        }),
        ('Profesionales presentes', {
            'fields': ('profesionales',)
        }),
    )
