from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from apps.partos.models.profesional import Profesional
# Importa el form que acabamos de crear
from apps.partos.forms.profesional_form import ProfesionalForm

class MenuInicioProfesionalesView(TemplateView):
    """Renderiza el menú de opciones de Profesionales"""
    template_name = 'partos/inicio_profesionales.html'

class ListarProfesionalesView(TemplateView):
    """Renderiza la tabla de profesionales"""
    # Cuando conectemos la BD, cambiaremos esto a ListView
    template_name = 'partos/listar_profesionales.html'

class CrearProfesionalView(CreateView):
    model = Profesional
    form_class = ProfesionalForm
    template_name = 'partos/formulario_profesionales.html'
    # Al terminar de agregar, nos lleva al listado para ver al nuevo integrante
    success_url = reverse_lazy('profesionales:listar')