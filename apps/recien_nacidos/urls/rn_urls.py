from django.urls import path

from ..views import CrearRecienNacidoView, AutoCompletadoDePartosView


app_name = "recien_nacido"

urlpatterns = [
    path('agregar/', CrearRecienNacidoView.as_view(), name="agregar_recien_nacido"),
    path('autocompletado/parto/', AutoCompletadoDePartosView.as_view(), name="autocompletar_parto")
]
