from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from core.mixins import MatronaSupervisorRequiredMixin
from ..models import Parto


class ListarPartosView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin, ListView):
    model = Parto
    template_name = ""
    permission_required = "partos.view_parto"
    raise_exception = True
    context_object_name = "partos"

    def get_queryset(self):
        return self.model.objects.select_related('gestacion__paciente')


