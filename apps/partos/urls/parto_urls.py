from django.urls import path

from ..views import ListarPartosView, CrearPartosView, AutoCompletadoParaGestacion, MenuInicioPartosView, ActualizarPartoView

app_name = "parto"

urlpatterns = [
    path('', MenuInicioPartosView.as_view(), name="inicio"),
    path('listar/', ListarPartosView.as_view(), name="listar_partos"),
    path('agregar/', CrearPartosView.as_view(), name="agregar_parto"),
    path('<int:pk>/actualizar/', ActualizarPartoView.as_view(), name="actualizar_parto"),
    path('autocompletado/gestacion', AutoCompletadoParaGestacion.as_view(), name="autocompletar_gestacion")
]


