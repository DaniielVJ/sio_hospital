# ROOT CONF URL
from django.contrib import admin
from django.urls import path, include
from apps.perfiles.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('pacientes/', include('apps.pacientes.urls.paciente')),
    path('gestaciones/', include('apps.pacientes.urls.gestacion')),
    path('partos/', include('apps.partos.urls')),
    path('perfiles/', include('apps.perfiles.urls')),
    path('rn/', include('apps.recien_nacidos.urls')),
    path('reportes/', include('apps.reportes.urls')),
]
