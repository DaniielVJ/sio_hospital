from django.urls import path

# 1. Vistas Generales de Parto (desde parto_views.py)
from ..views.parto_views import ( 
    ListarPartosView, 
    CrearPartosView, 
    AutoCompletadoParaGestacion, 
    MenuInicioPartosView, 
    ActualizarPartoView, 
    EliminarPartoView,
    DetallePartoModalView,
)

# 2. Vista Wizard (desde wizard_form_view.py)
from ..views.wizard_form_view import ( 
    WizardFormView,
)


app_name = "parto"

urlpatterns = [
    path('', MenuInicioPartosView.as_view(), name="inicio"),
    path('listar/', ListarPartosView.as_view(), name="listar_partos"),
    path('agregar/', CrearPartosView.as_view(), name="agregar_parto"),
    
    # URL de Detalle/Edición
    path('<int:pk>/detalle-modal/', DetallePartoModalView.as_view(), name="detalle_parto_modal"),
    path('<int:pk>/actualizar/', ActualizarPartoView.as_view(), name="actualizar_parto"),
    
    path('<int:pk>/eliminar/', EliminarPartoView.as_view(), name="eliminar_parto"),
    
    # URL de Autocompletado
    path('autocompletado/gestacion/', AutoCompletadoParaGestacion.as_view(), name="autocompletar_gestacion"),
    
    # URL Adicional (Wizard Form)
    path('wizard-form/', WizardFormView.as_view(), name="wizard_form"),
]