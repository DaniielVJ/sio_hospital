from django.views.generic import CreateView
from django.http import HttpResponse
from ..models import Gestacion
from ..forms import GestacionForm


class CrearGestacionView(CreateView):
    model = Gestacion
    template_name = "paciente/formulario_gestacion.html"
    form_class = GestacionForm
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        form.save()
        return HttpResponse('<h1>Gestacion Almacenada correctamente</h1>')



