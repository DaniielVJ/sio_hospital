from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Formulario para autenticar pero configurado para usar el Email como identificador
# para validar la identidad del usuario
class LoginEmailForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
    attrs={'placeholder': "Tu Correo Institucional"}
    ))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['placeholder'] = "••••••••"
        self.fields['username'].label = "Email"
