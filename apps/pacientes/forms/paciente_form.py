from django import forms
from ..models import Paciente
from . import validators
from . import utils

class PacienteForm(forms.ModelForm):        
    class Meta:
        model = Paciente
        exclude = ['fecha_ingreso', 'id']
        widgets = {
           'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'})
        }

        help_texts = {
            'cesfam': 'Si no posee dejar en blanco',
            'comuna': 'Si no aparece la comuna dejar en blanco'
            }


    def clean(self):
        cleaned = super().clean()
        documento = cleaned.get('documento')
        identificacion = cleaned.get('identificacion')

        # RECORDAR EL CLEANED DATA YA ES VALIDADA Y COMO SE ALMACENARA EN LA DB
        # POR ESO EN MAYUSCULA
        if documento == "RUT":
            if not identificacion:
                raise forms.ValidationError('Debe proporcionar el rut')
            validators.validar_rut(identificacion)
        elif documento == "PAS":
            if not identificacion or len(identificacion) < 5:
                raise forms.ValidationError('Debe proporcionar el pasaporte completo')
        elif documento == "EXT":
            if not identificacion or len(identificacion) < 3:
                raise forms.ValidationError('Debe proporcionar codigo extranjero')
        elif documento == "TMP":
            codigo_temporal = utils.generar_codigo_temporal()
            cleaned['identificacion'] = codigo_temporal
        else:
            forms.ValidationError('Debe seleciona un tipo de documento')
    
        return cleaned