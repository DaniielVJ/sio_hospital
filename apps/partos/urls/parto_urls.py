from django.urls import path

from ..views import ListarPartosView, CrearPartosView

app_name = "parto"

urlpatterns = [
    path('listar/', ListarPartosView.as_view(), name="listar_partos"),
    path('agregar/', CrearPartosView.as_view(), name="agregar_parto")
]


