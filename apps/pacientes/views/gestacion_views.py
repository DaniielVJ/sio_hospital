from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse

from core.mixins import MatronaSupervisorRequiredMixin
from ..models import Gestacion
from ..forms import GestacionForm



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
    

class CrearGestacionView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin, CreateView):
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



