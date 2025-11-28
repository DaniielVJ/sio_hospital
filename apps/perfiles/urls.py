from django.urls import path
from .views import ModificarPasswordView


app_name = "perfiles"

urlpatterns = [
    path('modificar-password/', ModificarPasswordView.as_view(), name='modificar_password'),
]
