from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from dal import autocomplete
from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from core.mixins import MatronaSupervisorRequiredMixin, MatronaRequiredMixin
from ..models import Parto
from apps.pacientes.models import Gestacion
from ..forms import PartoForm


class ListarPartosView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin, ListView):
    model = Parto
    template_name = ""
    permission_required = "partos.view_parto"
    raise_exception = True
    context_object_name = "partos"

    def get_queryset(self):
        return self.model.objects.select_related('gestacion__paciente')


class CrearPartosView(MatronaRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Parto
    template_name = "partos/formulario_parto.html"
    permission_required = "partos.add_parto"
    raise_exception = True
    form_class = PartoForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    

# View para autocompletar la busqueda del formulario Partos para el campo gestacion/gestaciones
class AutoCompletadoParaGestacion(MatronaRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        gestaciones = Gestacion.objects.all()
        

        if self.q:
            gestaciones = gestaciones.annotate(nombre_completo_paciente=Concat('paciente__nombre', Value(' '), 'paciente__primer_apellido', Value(' '), 'paciente__segundo_apellido'), 
                                               identificacion_paciente=F('paciente__identificacion'))
            # Aqui igual puede ser: paciente__identificacion__startswith=self.q
            return gestaciones.filter(Q(nombre_completo_paciente__icontains=self.q) | Q(identificacion_paciente__startswith=self.q) | Q(pk__startswith=self.q)).order_by('nombre_completo_paciente')
        return gestaciones.none()