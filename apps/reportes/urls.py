from django.urls import path

from apps.reportes.views.inicio_views import inicio_reportes
from .views import GenerarReporteCesarea

app_name = "reportes"

urlpatterns = [
    path('cesarea/', GenerarReporteCesarea.as_view(), name="crear_reporte_cesarea"),
    path('', inicio_reportes, name='inicio_reportes'),
]
