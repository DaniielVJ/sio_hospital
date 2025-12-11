from django.shortcuts import render

def inicio_reportes(request):
    """
    Vista para renderizar el Dashboard principal de Reportes.
    """
    return render(request, 'reportes/inicio_reportes.html')