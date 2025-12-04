from django.views.generic import CreateView
from ..models import TestHepatitisB, TestSgb, TestVdrl, TestVih
from ..forms import TestHepatitisBForm, TestSgbForm, TestVdrlForm, TestVihForm

# Recordar que para simplificar todos renderizan el formulario en el mismo template
# porque hacen un .as_div, pero luego debe haber un template personalizado por cada Test
# porque no todos tienen los mismo campos y los renderizaremos de forma individual
class CrearTestHepatitisBView(CreateView):
    model=TestHepatitisB
    template_name = "paciente/formulario_tests.html"
    form_class = TestHepatitisBForm


class CrearTestSgbView(CreateView):
    model=TestSgb
    template_name = "paciente/formulario_tests.html"
    form_class = TestSgbForm


class CrearTestVdrlForm(CreateView):
    model=TestVdrl
    template_name = "paciente/formulario_tests.html"
    form_class = TestVdrlForm


class CrearTestVihForm(CreateView):
    model=TestVih
    template_name = "paciente/formulario_tests.html"
    form_class = TestVihForm



