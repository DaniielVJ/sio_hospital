from django.urls import path

from ..views import CrearRecienNacidoView


app_name = "recien_nacido"

urlpatterns = [
    path('agregar/', CrearRecienNacidoView.as_view(), name="agregar_recien_nacido")
]
