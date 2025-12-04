from django.utils import timezone
from django import forms
from django.forms.utils import ErrorList
import phonenumbers

from ..models import Paciente
from . import validators
from . import utils


class PacienteForm(forms.ModelForm):
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
        exclude = ['created_by', 'created_at', 'updated_by', 'updated_at']

        # Textos mostrados debajo de cada campo al renderizarlo
        help_texts = {
            'cesfam': 'Si no posee dejar en blanco',
            'comuna': 'Si no aparece la comuna dejar en blanco',
            'identificacion': 'Si es Rut sin puntos y con guion',
            'altura': 'En centimetros',
            'peso': 'En Kilogramos',
            'telefono': 'Para números nacionales NO ES OBLIGATORIO usar el código +56 añada el 9',
            'nacionalidad': "Si no aparece la nacinalidad marcar OTRA"
            }
        
        widgets = {
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Dirección del paciente',
                'maxlength': 150,
                }),
            'telefono': forms.TextInput(attrs={
                'placeholder': 'Telefono del paciente',
                'maxlength': 15,
                'minlength': 5
            }),
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del Paciente',
                'maxlength': 100,
                'minlength': 5,
                'required': ''
            })
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


    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        
        if not peso:
            return peso

        if not peso > 0:
            raise forms.ValidationError("Una persona no puede pesar menos de 0")
        return peso


    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if not altura:
            return altura
        
        if not altura > 0:
            raise forms.ValidationError("Una persona no puede ser un minion")
        
        return altura


    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono:
            return telefono


        try:
            if telefono.startswith("+"):
                telefono_parseado = phonenumbers.parse(telefono)
            else:
                # si viene sin + asumiremos que es chileno aunque no lo sea
                telefono_parseado = phonenumbers.parse(telefono, "CL")
        except phonenumbers.NumberParseException as e:
            # Si fallo el parse puede ser por estos motivos:
            if e.error_type == e.INVALID_COUNTRY_CODE:
                raise forms.ValidationError("Codigo de pais invalido para el numero proporcionado")
            elif e.error_type == e.NOT_A_NUMBER:
                raise forms.ValidationError("El número telefonico no puede contener letras")
            elif e.error_type == e.TOO_LONG:
                raise forms.ValidationError("El número es demasiado largo para ser valido")
            elif e.error_type == e.TOO_SHORT_NSN or e.error_type == e.TOO_SHORT_AFTER_IDD:
                raise forms.ValidationError("El número es demasiado corto para ser valido")
            else:
                raise forms.ValidationError("El número no es valido")
            
        # Una vez tenemos el nùmero parseado en un formato valido y soportado por la libreria
        # evaluamos si ese número podria existir en ese pais que se especifico por su codigo
        # si regresa False es pq es imposible que exista como +56 9 11111111 que cumple la estructura de chile
        # pero no es valido
        if not phonenumbers.is_valid_number(telefono_parseado):
            raise forms.ValidationError("El número no es valido. Ingrese un numero que pueda existir en el pais")

        # Si pasa las validaciones lo regresamos en el formato aceptado internacionalmente E.164 que es usado
        # en todos los sistemas como GMAIL, WHATSAPP, ANDROID.
        return phonenumbers.format_number(
            telefono_parseado, 
            phonenumbers.PhoneNumberFormat.E164
        )
        

        
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data["fecha_nacimiento"]
        fecha_actual = timezone.now().date()

        if fecha_nacimiento > fecha_actual:
            return forms.ValidationError('La fecha de nacimiento no puede superar a la fecha actual')
        
        return fecha_nacimiento
    


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