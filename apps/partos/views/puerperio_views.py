from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404

from core.mixins import MatronaRequiredMixin
from ..forms import PuerperioForm
from ..models import Puerperio, Parto



class CreatePuerperioView(MatronaRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Puerperio
    form_class = PuerperioForm
    template_name = 'partos/formulario_puerperio.html'
    permission_required = 'partos.add_puerperio'
    raise_exception = True
    # modify success url to detail childbirth 
    success_url = reverse_lazy('parto:listar_partos')

    
    def form_valid(self, form):
        parto = get_object_or_404(Parto, pk=self.kwargs.get('pk_parto'))
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        form.instance.parto = parto
        messages.success(self.request, "Puerperio añadido al parto exitosamente")
        return super().form_valid(form)
    