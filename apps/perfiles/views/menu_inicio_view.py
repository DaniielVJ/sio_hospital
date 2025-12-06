from django.views.generic import TemplateView
from core.mixins import MatronaSupervisorRequiredMixin, AdminTiRequiredMixin

class MostrarPantallaPrincipalView(AdminTiRequiredMixin, TemplateView):
    template_name="principal.html"
