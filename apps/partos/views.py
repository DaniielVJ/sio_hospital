from django.shortcuts import render
from .forms import PartoForm

# Create your views here.


def probar_form_partos(request):
    form = PartoForm()
    return render(request, 'parto/formulario_parto.html', {'form': form})