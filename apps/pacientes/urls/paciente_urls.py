from django.urls import path
from .. import views




app_name = "paciente"

urlpatterns = [
    path('', views.MostrarMenuInicioPaciente.as_view(), name="inicio"),
    path('list/', views.ListarPacientesView.as_view(), name="listar_pacientes"),
    path('<int:pk>/detalle/', views.DetallePacienteView.as_view(), name="detalle_paciente"),
    path('agregar/', views.CrearPacienteView.as_view(), name="agregar_paciente"),
    path('<int:pk>/actualizar/', views.ActualizarPacienteView.as_view(), name="actualizar_paciente"),
    path('<int:pk>/eliminar/', views.EliminarPacienteView.as_view(), name="eliminar_paciente"),
]
