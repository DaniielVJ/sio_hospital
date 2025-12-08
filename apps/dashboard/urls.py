from django.urls import path
from .views import vistas_views, kpis_views, graficos_views, tablas_views

urlpatterns = [
    path('', vistas_views.index, name='dashboard_index'),
    path('test/', vistas_views.TestView.as_view(), name='dashboard_test'),
    path('kpis/', kpis_views.KpisJsonView.as_view(), name='kpis'),
]

