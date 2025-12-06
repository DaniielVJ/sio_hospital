from django.views.generic import TemplateView
from core.mixins import MatronaSupervisorRequiredMixin, AdminTiRequiredMixin

class MostrarPantallaPrincipalView(MatronaSupervisorRequiredMixin, TemplateView):
    template_name="principal.html"
