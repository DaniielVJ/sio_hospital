from django.urls import path

from ..views import ListarPartosView

app_name = "parto"

urlpatterns = [
    path('listar/', ListarPartosView.as_view(), name="listar_partos")
]


