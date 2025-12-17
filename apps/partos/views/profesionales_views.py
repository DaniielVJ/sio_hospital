from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from core.mixins import MatronaRequiredMixin, MatronaSupervisorRequiredMixin


from apps.partos.models.profesional import Profesional
# Importa el form que acabamos de crear
from apps.partos.forms.profesional_form import ProfesionalForm

class MenuInicioProfesionalesView(MatronaSupervisorRequiredMixin, TemplateView):
    """Renderiza el menú de opciones de Profesionales"""
    template_name = 'partos/inicio_profesionales.html'

class ListarProfesionalesView(MatronaSupervisorRequiredMixin, ListView):
    """Renderiza la tabla de profesionales"""
    model = Profesional
    template_name = 'partos/listar_profesionales.html'
    context_object_name = 'profesionales' # Al ser ListView, ahora sí enviará esta variable
    paginate_by = 10
    
class CrearProfesionalView(MatronaRequiredMixin, CreateView):
    model = Profesional
    form_class = ProfesionalForm
    template_name = 'partos/formulario_profesionales.html'
    # Al terminar de agregar, nos lleva al listado para ver al nuevo integrante
    success_url = reverse_lazy('profesionales:listar')