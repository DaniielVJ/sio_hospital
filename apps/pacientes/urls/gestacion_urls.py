from django.urls import path
from ..views import CrearGestacionView


app_name = "gestacion"


urlpatterns = [
    path('add/', CrearGestacionView.as_view(), name="crear_gestacion")
]
