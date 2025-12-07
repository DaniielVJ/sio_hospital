from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('maingrafic/', views.DashboardView.as_view(), name='dashboard_main'),
    path('graphic2/', views.Graphic2View.as_view(), name='dashboard_graphic2'),
    path('test/', views.TestView.as_view(), name='dashboard_test'),
]

