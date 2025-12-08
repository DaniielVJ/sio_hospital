from django.urls import path
from ..views import CrearGestacionView, ListarGestacionesView, AutoCompletadoDePaciente


app_name = "gestacion"


urlpatterns = [
    path('listar/', ListarGestacionesView.as_view(), name="listar_gestaciones"),
    path('agregar/', CrearGestacionView.as_view(), name="crear_gestacion"),
    path('autocomplete/paciente/', AutoCompletadoDePaciente.as_view(), name='autocompletar_paciente')
]
