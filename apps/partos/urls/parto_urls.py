from django.urls import path
<<<<<<< HEAD
from ..views import (
    ListarPartosView, CrearPartosView, AutoCompletadoParaGestacion, 
    MenuInicioPartosView, ActualizarPartoView, EliminarPartoView
)
=======

from ..views import ListarPartosView, CrearPartosView, AutoCompletadoParaGestacion, MenuInicioPartosView, ActualizarPartoView, EliminarPartoView, WizardFormView
>>>>>>> 2ce7f1977af4f8d7f0a9c961e764e5fe7dcb73cf

app_name = "parto"

urlpatterns = [
    path('', MenuInicioPartosView.as_view(), name="inicio"),
    path('listar/', ListarPartosView.as_view(), name="listar_partos"),
    path('agregar/', CrearPartosView.as_view(), name="agregar_parto"),
    path('<int:pk>/actualizar/', ActualizarPartoView.as_view(), name="actualizar_parto"),
    path('<int:pk>/eliminar/', EliminarPartoView.as_view(), name="eliminar_parto"),
<<<<<<< HEAD
    path('autocompletado/gestacion/', AutoCompletadoParaGestacion.as_view(), name="autocompletar_gestacion")
]
=======
    path('autocompletado/gestacion/', AutoCompletadoParaGestacion.as_view(), name="autocompletar_gestacion"),
    # wizard_url
    path('wizard-form/', WizardFormView.as_view(), name="wizard_form"),
]


>>>>>>> 2ce7f1977af4f8d7f0a9c961e764e5fe7dcb73cf
