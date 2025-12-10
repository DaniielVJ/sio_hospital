from django.urls import path

from ..views import CrearRecienNacidoView, AutoCompletadoDePartosView, MenuInicioRecienNacido, ListarRecienNacidoView


app_name = "recien_nacido"

urlpatterns = [
    path('', MenuInicioRecienNacido.as_view(), name="inicio"),
    path('listar/', ListarRecienNacidoView.as_view(), name="listar_recien_nacidos"),
    path('agregar/', CrearRecienNacidoView.as_view(), name="agregar_recien_nacido"),
    path('autocompletado/parto/', AutoCompletadoDePartosView.as_view(), name="autocompletar_parto")
]
