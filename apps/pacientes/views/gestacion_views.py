from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.db.models import Q, Value
from django.db.models.functions import Concat
from dal import autocomplete

from core.mixins import MatronaSupervisorRequiredMixin, MatronaRequiredMixin
from ..models import Gestacion, Paciente
from ..forms import GestacionForm



class MenuInicioGestacionesView(MatronaSupervisorRequiredMixin, TemplateView):
    template_name = "pacientes/inicio_gestaciones.html"


class ListarGestacionesView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin,ListView):
    model = Gestacion
    template_name = ""
    context_object_name = 'gestaciones'
    paginate_by = 10

    permission_required = "pacientes.view_gestacion"
    raise_exception = True

    # Por cada una de las 10 o 15 gestaciones listadas en la pagina se precarga el paciente que tiene asociado
    def get_queryset(self):
        return self.model.objects.select_related('paciente')
    

class CrearGestacionView(MatronaRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Gestacion
    template_name = "pacientes/formulario_gestacion.html"
    form_class = GestacionForm
    
    permission_required = "pacientes.add_gestacion"
    raise_exception = True

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        form.save()
        return HttpResponse('<h1>Gestacion Almacenada correctamente</h1>')



# View de autocompletado para el formulario de gestacion
class AutoCompletadoDePaciente(MatronaRequiredMixin, autocomplete.Select2QuerySetView):
    # Esta view en cada input o change que se detecte el formulario en el navegador recibira ese valor y ejecutara la logica
    # del metodo get_queryset para ir autocompletando al usuario con el resultado o queryset que regrese este metodo.
    def get_queryset(self):
        query = self.q
        pacientes = Paciente.objects.all()
        
        if query:
            # annotate permite añadirle a todos los objetos del queryset un nuevo campo o field temporal que solo dura en la ejecucion del codigo
            # que almacena el resultado de una operacion, en este caso el proceso de concatenar el nombre  y los apellidos de los paciente para luego filtrar por
            # ese nuevo field de nombre_completo
            pacientes = pacientes.annotate(nombre_completo=Concat('nombre', Value(' '), 'primer_apellido', Value(' '), 'segundo_apellido'))
            return pacientes.filter(Q(identificacion__startswith=query) | Q(nombre_completo__icontains=query))
        return pacientes.none()



