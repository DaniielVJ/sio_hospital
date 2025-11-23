from django import forms
from django.forms.utils import ErrorList

from ..models import Paciente
from . import validators
from . import utils



class MyErrorList(ErrorList):
    def as_divs(self):
        return ''.join(f'<div class="text-red-600 text-sm mt-1">{e}</div>' for e in self)

    def __str__(self):
        return self.as_divs()


class PacienteForm(forms.ModelForm):
    error_class = MyErrorList

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields['tipo'].widget)
        for nombre_campo, campo  in self.fields.items():
            widget = campo.widget
            # Si quiero añadir mas clases, las voy agregando simplemente aqui
            if isinstance(widget, forms.widgets.CheckboxInput):
                widget.attrs['class'] = 'form-check-input'
            elif isinstance(widget, forms.Select):
                widget.attrs['class'] = 'form-select'
            else:
                widget.attrs['class'] = 'form-control'
        
       
    class Meta:
        model = Paciente
        exclude = ['fecha_ingreso', 'id']
        widgets = {
           'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'})
        }

        # Textos mostrados debajo de cada campo al renderizarlo
        help_texts = {
            'cesfam': 'Si no posee dejar en blanco',
            'comuna': 'Si no aparece la comuna dejar en blanco',
            'identificacion': 'Si es Rut sin puntos y con guion',
            'altura': 'En centimetros',
            'peso': 'En Kilogramos'
            }
        
        # El texto del label que describe o indica que valor recibe el campo
        labels = {
            'documento': "Tipo Documento",
            'identificacion': 'N° de documento',
            'tipo': 'Tipo de Paciente',
            'descapacitado': 'Descapacitad@',
            'pueblo_originario': 'Pueblo Originario',
            'privada_de_libertad': 'Privada de Libertad',
            'transexual': 'Transexual',
            'fecha_nacimiento': 'Drogadicto'
            
        }


    def clean(self):
        cleaned = super().clean()
        documento = cleaned.get('documento')
        identificacion = cleaned.get('identificacion')

        # RECORDAR EL CLEANED ES DATA YA ES VALIDADA Y COMO SE ALMACENARA EN LA DB
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