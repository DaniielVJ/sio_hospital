from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Formulario para autenticar pero configurado para usar el Email como identificador
# para validar la identidad del usuario
class LoginEmailForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))