from django.contrib import admin
from ..models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):

    list_display = ('documento','identificacion','obtener_nombre_completo','tipo','nacionalidad','comuna','cesfam','telefono','fecha_nacimiento','descapacitado',)

    search_fields = ('identificacion','nombre','primer_apellido','segundo_apellido','telefono','comuna__nombre','cesfam__nombre',)

    list_filter = ('tipo','nacionalidad','comuna','cesfam','descapacitado','pueblo_originario','privada_de_libertad','transexual','plan_de_parto','visita_guiada','actividad','fecha_nacimiento',)

    ordering = ('primer_apellido', 'segundo_apellido', 'nombre')
    list_per_page = 20
    readonly_fields = ('fecha_ingreso',)

    fieldsets = (
        ('Identificación', {
            'fields': ('documento', 'identificacion')
        }),
        

        ('Datos Personales', {
            'fields': ('nombre', 'primer_apellido', 'segundo_apellido','fecha_nacimiento', 'nacionalidad','comuna', 'cesfam', 'direccion', 'telefono')
        }),
        

        ('Situación Especial', {
            'fields': ('descapacitado','pueblo_originario','privada_de_libertad','transexual',)
        }),


        ('Parto y Planificación', {
            'fields': ('plan_de_parto', 'visita_guiada')
        }),


        ('Datos Clínicos', {
            'fields': ('peso', 'altura', 'actividad')
        }),

        
        ('Información del Sistema', {
            'fields': ('fecha_ingreso',),
            'classes': ('collapse',)
        })
    )
