from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from..forms import PacienteForm
from ..models import Paciente



# View encargada de listar todos los pacientes al usuario que lo solicite
class ListarPacientesView(ListView):
    model = Paciente
    template_name = 'pacientes/listar_pacientes.html'
    context_object_name = 'pacientes'


    def get_queryset(self):
        # Por ahora se entregan todos los pacientes a todas las matronas, despues vemos si filtramos
        qs =  Paciente.objects.select_related('tipo', 'comuna', 'nacionalidad')
        return qs


class DetallePacienteView(DetailView):
    model = Paciente
    template_name = 'pacientes/detalle_paciente.html'
    context_object_name = 'paciente'

    def get_queryset(self):
        qs = Paciente.objects.select_related('tipo', 'comuna', 'nacionalidad', 'cesfam')
        return qs

# View para añadir o crear un nuevo Paciente en el servidor
class CrearPacienteView(CreateView):
    model = Paciente
    template_name = 'pacientes/formulario_paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('pacientes:listar_pacientes')

    

class ActualizarPacienteView(UpdateView):
    pass


class EliminarPacienteView(DeleteView):
    pass