from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from..forms import PacienteForm
from ..models import Paciente



# View encargada de listar todos los pacientes al usuario que lo solicite
class ListarPacientesView(ListView):
    model = Paciente
    template_name = 'paciente/listar_pacientes.html'
    context_object_name = 'pacientes'


    def get_queryset(self):
        # Por ahora se entregan todos los pacientes a todas las matronas, despues vemos si filtramos
        qs =  self.model.objects.select_related('tipo', 'comuna', 'nacionalidad')
        return qs


# View encargada de mostrar los detalles de cada paciente
class DetallePacienteView(DetailView):
    model = Paciente
    template_name = 'paciente/detalle_paciente.html'
    context_object_name = 'paciente'

    def get_queryset(self):
        qs = self.model.objects.select_related('tipo', 'comuna', 'nacionalidad', 'cesfam')
        return qs


# View para añadir o crear un nuevo Paciente en el servidor
class CrearPacienteView(CreateView):
    model = Paciente
    template_name = 'paciente/formulario_paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('pacientes:listar_pacientes')

    
# view encargada se ejecutar la logica para actualizar los datos de un paciente
class ActualizarPacienteView(UpdateView):
    pass


# view encargada de ejecutar la logica para eliminar un objeto del modelo
class EliminarPacienteView(DeleteView):
    pass



