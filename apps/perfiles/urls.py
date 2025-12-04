from django.urls import path
from .views import ModificarPasswordView, VerificarCodigoPorEmailView


app_name = "perfiles"

urlpatterns = [
    path('modificar-password/', ModificarPasswordView.as_view(), name='modificar_password'),
    path('verificacion-email/', VerificarCodigoPorEmailView.as_view(), name="verificar_codigo_email")
]
