from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')

class PacientesView(TemplateView):
    template_name = 'layouts/pacientes.html'

class PartosView(TemplateView):
    template_name = 'layouts/partos.html'

class PerfilesView(TemplateView):
    template_name = 'layouts/perfiles.html'

class RecienNacidosView(TemplateView):
    template_name = 'layouts/recien_nacidos.html'

class ReportesView(TemplateView):
    template_name = 'layouts/reportes.html'

class ProfesionalesView(TemplateView):
    template_name = 'layouts/profesionales.html'


class TestView(TemplateView):
    template_name = '500.html'


