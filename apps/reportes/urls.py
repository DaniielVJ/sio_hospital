from django.urls import path
from .views import GenerarReporteCesarea

app_name = "reportes"

urlpatterns = [
    path('cesarea/', GenerarReporteCesarea.as_view(), name="crear_reporte_cesarea")
]
