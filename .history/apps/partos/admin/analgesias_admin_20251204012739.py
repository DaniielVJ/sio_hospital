from django.contrib import admin
from ..models import Analgesias

@admin.register(AnalgesiaParto)
class AnalgesiaPartoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'parto',
        'tipo',
        'solicitada',
        'indicada',
        'administrada',
        'created_at',
    )

    list_filter = (
        'tipo',
        'solicitada',
        'indicada',
        'administrada',
    )

    search_fields = (
        'parto__id',
        'tipo__nombre',
        'created_by__username',
    )

    autocomplete_fields = ('parto', 'tipo')

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fieldsets = (
        ('Información general', {
            'fields': (
                'parto',
                'tipo',
            )
        }),

        ('Detalles de la analgesia', {
            'fields': (
                'solicitada',
                'indicada',
                'administrada',
                'tiempo_espera_minutos',
                'dosis',
                'notas',
            )
        }),

        ('Registro del Sistema', {
            'fields': (
                'created_at',
                'created_by',
            ),
            'classes': ('collapse',)
        }),
    )
