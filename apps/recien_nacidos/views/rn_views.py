from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from dal import autocomplete
from django.db.models.functions import Concat
from django.db.models import Value, Q, F

from ..forms import RecienNacidoForm
from ..models import RecienNacido
from apps.partos.models import Parto
from core.mixins import MatronaRequiredMixin, MatronaSupervisorRequiredMixin


class CrearRecienNacidoView(MatronaRequiredMixin, PermissionRequiredMixin, CreateView):
    model = RecienNacido
    template_name = "recien_nacidos/formulario_rn.html"
    form_class = RecienNacidoForm
    permission_required = "recien_nacidos.add_reciennacido"
    raise_exception = True

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)




class AutoCompletadoDePartosView(MatronaRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        partos = Parto.objects.all()

        if self.q:
            partos = partos.annotate(nombre_completo_paciente=Concat('gestacion__paciente__nombre', Value(' '), 'gestacion__paciente__primer_apellido', Value(' '), 'gestacion__paciente__segundo_apellido'),
                                     identificacion_paciente=F('gestacion__paciente__identificacion'))
            
            return partos.filter(Q(nombre_completo_paciente__icontains=self.q) | Q(identificacion_paciente__startswith=self.q) | Q(pk__startswith=self.q))
        
        return partos.none()