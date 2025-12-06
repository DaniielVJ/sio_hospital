from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse

from core.mixins import MatronaSupervisorRequiredMixin
from ..models import Gestacion
from ..forms import GestacionForm



class ListarGestacionesView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin,ListView):
    model = Gestacion
    permission_required = "pacientes.view_gestacion"
    template_name = ""
    raise_exception = True

    # Por cada una de las 10 o 15 gestaciones listadas en la pagina se precarga el paciente que tiene asociado
    def get_queryset(self):
        return self.model.objects.select_related('paciente')
    

class CrearGestacionView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Gestacion
    template_name = "paciente/formulario_gestacion.html"
    form_class = GestacionForm
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        form.save()
        return HttpResponse('<h1>Gestacion Almacenada correctamente</h1>')



