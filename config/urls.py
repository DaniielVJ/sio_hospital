# ROOT CONF URL
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from apps.perfiles.views import LoginView

from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('pacientes/', include('apps.pacientes.urls.paciente')),
    path('gestaciones/', include('apps.pacientes.urls.gestacion')),
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
        path("__reload__/", include("django_browser_reload.urls")),
        path('tailwind/', tailwind_testear)
    ]


