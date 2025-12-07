from django import forms
from django.utils import timezone
from ..models import Parto


class PartoForm(forms.ModelForm):

    tiempo_membrana_rota = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'placeholder': 'En minutos'
    }), help_text="Tiempo en minutos", required=True)

    tiempo_dilatacion = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'placeholder': 'En minutos'
    }), help_text="Tiempo en minutos", required=True)

    tiempo_expulsivo = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'placeholder': 'En minutos'
    }), help_text="Tiempo en minutos", required=True)


    class Meta:
        model = Parto
        exclude = [
            'created_by', 'created_at', 'updated_by', 'updated_at',
            'edad_madre'
            ]
        widgets = {
            'complicaciones': forms.CheckboxSelectMultiple()
        }

    def clean_tiempo_membrana_rota(self):
        tiempo_membrana_rota = self.cleaned_data.get('tiempo_membrana_rota')
        tiempo_membrana_rota = timezone.timedelta(minutes=tiempo_membrana_rota)
        return tiempo_membrana_rota

    
    def clean_tiempo_dilatacion(self):
        tiempo_dilatacion = self.cleaned_data.get('tiempo_dilatacion')
        tiempo_dilatacion = timezone.timedelta(minutes=tiempo_dilatacion)
        return tiempo_dilatacion
    

    def clean_tiempo_expulsivo(self):
        tiempo_expulsivo = self.cleaned_data.get('tiempo_expulsivo')
        tiempo_expulsivo = timezone.timedelta(minutes=tiempo_expulsivo)
        return tiempo_expulsivo
    
    def clean(self):
        cleaned_data =  super().clean()
        via_nacimiento = cleaned_data.get('via_nacimiento')
        grupo_robson = cleaned_data.get('grupo_robson')
        
        if via_nacimiento:
            if (via_nacimiento.tipo == "CES.ELECTIVA" or via_nacimiento.tipo == "CES. URGENCIA") and not (grupo_robson):
                self.add_error('grupo_robson', 'Si la via de nacimiento es por cesarea debe añadir grupo robson')
            elif (via_nacimiento.tipo == "EUTOCICO" or via_nacimiento.tipo == "DISTOCICO") and grupo_robson:
                self.add_error('grupo_robson', 'El grupo robson solo debe estar marcado en los partos por cesarea')
        return cleaned_data