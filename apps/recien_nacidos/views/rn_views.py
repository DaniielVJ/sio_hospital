from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..forms import RecienNacidoForm
from ..models import RecienNacido
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
    