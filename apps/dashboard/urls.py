from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('maingrafic/', views.DashboardView.as_view(), name='dashboard_main'),
    path('test/', views.TestView.as_view(), name='dashboard_test'),
]

