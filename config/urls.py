# ROOT CONF URL
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('apps.pacientes.urls')),
    path('partos/', include('apps.partos.urls')),
    path('perfiles/', include('apps.perfiles.urls')),
    path('rn/', include('apps.recien_nacidos.urls')),
    path('reportes/', include('apps.reportes.urls')),
]
