# ROOT CONF URL
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings

from apps.perfiles.views import LoginView, MostrarPantallaPrincipalView





urlpatterns = [
    path('', MostrarPantallaPrincipalView.as_view(), name="pantalla_principal"),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('pacientes/', include('apps.pacientes.urls.paciente_urls')),
    path('gestaciones/', include('apps.pacientes.urls.gestacion_urls')),
    path('tests/', include('apps.pacientes.urls.test_urls')),
    path('partos/', include('apps.partos.urls')),
    path('perfiles/', include('apps.perfiles.urls')),
    path('rn/', include('apps.recien_nacidos.urls')),
    path('reportes/', include('apps.reportes.urls')),
    
]

if settings.DEBUG:
    from django.shortcuts import render
    def tailwind_testear(request):
        return render(request, 'tailwindsito.html')

    urlpatterns += [
        path('tailwind/', tailwind_testear)
    ]


