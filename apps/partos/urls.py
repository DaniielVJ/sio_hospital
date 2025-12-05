from django.urls import path
from . import views

app_name = "partos"

urlpatterns = [
    path('add/', views.probar_form_partos)
]
