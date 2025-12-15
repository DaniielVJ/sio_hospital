from django.urls import path
from .views import vistas_views
urlpatterns = [
    path('', vistas_views.index, name='dashboard_index'),
    path('pacientes/', vistas_views.PacientesView.as_view(), name='dashboard_pacientes'),
    path('partos/', vistas_views.PartosView.as_view(), name='dashboard_partos'),
    path('recien_nacidos/', vistas_views.RecienNacidosView.as_view(), name='dashboard_rnacidos'),
    path('profesionales/', vistas_views.ProfesionalesView.as_view(), name='dashboard_profesionales'),
    path('reportes/', vistas_views.ReportesView.as_view(), name='dashboard_reportes'),
]

