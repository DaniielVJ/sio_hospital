from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from core.mixins import MatronaSupervisorRequiredMixin, MatronaRequiredMixin
from ..models import Parto
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
    