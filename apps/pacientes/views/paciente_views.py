from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from core.mixins import MatronaRequiredMixin, SupervisorRequiredMixin, MatronaSupervisorRequiredMixin
from ..forms import PacienteForm
from ..models import Paciente



class MostrarMenuInicioPaciente(MatronaSupervisorRequiredMixin, TemplateView):
    template_name="pacientes/menu_inicio_paciente.html"


# View encargada de listar todos los pacientes al usuario que lo solicite
class ListarPacientesView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin, ListView):
    model = Paciente
    permission_required = "pacientes.view_paciente"
    raise_exception = True
    template_name = 'pacientes/listar_pacientes.html'
    context_object_name = 'pacientes'
    paginate_by = 10    

    def get_queryset(self):
        # Por ahora se entregan todos los pacientes a todas las matronas, despues vemos si filtramos
        qs =  self.model.objects.select_related('tipo', 'comuna', 'nacionalidad')
        return qs


# View encargada de mostrar los detalles de cada paciente
class DetallePacienteView(MatronaSupervisorRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Paciente
    permission_required = "pacientes.view_paciente"
    raise_exception = True
    template_name = 'pacientes/detalle_paciente.html'
    context_object_name = 'paciente'

    def get_queryset(self):
        qs = self.model.objects.select_related('tipo', 'comuna', 'nacionalidad', 'cesfam')
        return qs



# View para añadir o crear un nuevo Paciente en el servidor
class CrearPacienteView(MatronaRequiredMixin, CreateView):
    model = Paciente
    template_name = 'pacientes/formulario_paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('paciente:listar_pacientes')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        messages.success(self.request, 'Paciente creado correctamente')
        return super().form_valid(form)

    
# view encargada se ejecutar la logica para actualizar los datos de un paciente
class ActualizarPacienteView(UpdateView):
    pass


# view encargada de ejecutar la logica para eliminar un objeto del modelo
class EliminarPacienteView(DeleteView):
    pass



