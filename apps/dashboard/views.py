from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')

class DashboardView(TemplateView):
    template_name = 'componentes/maingrafic.html'

class TestView(TemplateView):
    template_name = '500.html'
