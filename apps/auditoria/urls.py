from django.urls import path
from . import views

app_name = "auditoria"


urlpatterns = [
    path('', views.MenuInicioAuditoriaView.as_view(), name="inicio"),
    # pacientes audit
    path('pacientes/', views.ListarHistoricoPaciente.as_view(), name="historicos_pacientes"),
    path('paciente/<int:id_paciente>/historico/<str:tipo>/<int:pk>', views.CargarInfoHistoricoPacienteView.as_view(), name="historico_paciente"),
    # gestaciones audit
    path('gestaciones/', views.ListarHistoricoGestaciones.as_view(), name="historicos_gestaciones"),
    # partos audit
    path('partos/', views.ListarHistoricoPartos.as_view(), name="historicos_partos"),
    # recien nacidos audit
    path('rns/', views.ListarHistoricoRecienNacidos.as_view(), name="historicos_recien_nacidos")


]
