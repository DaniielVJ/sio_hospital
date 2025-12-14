from django.urls import path
# Importamos las vistas desde tu carpeta views
from apps.partos.views.profesionales_views import MenuInicioProfesionalesView, ListarProfesionalesView, CrearProfesionalView

# LE DAMOS SU PROPIO NOMBRE DE APP (NAMESPACE)
app_name = "profesionales"

urlpatterns = [

    path('', MenuInicioProfesionalesView.as_view(), name="inicio"),
    path('listar/', ListarProfesionalesView.as_view(), name="listar"),
    path('agregar/', CrearProfesionalView.as_view(), name="agregar"),

]