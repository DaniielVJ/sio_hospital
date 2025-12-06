from django import forms
from ..models import RecienNacido


class RecienNacidoForm(forms.ModelForm):
    class Meta:
        model = RecienNacido
        exclude = ['created_by', 'created_at', 'updated_by', 'updated_at']



   # ACORDARSE AÑADIR LAS VALIDACIONES LUEGO
