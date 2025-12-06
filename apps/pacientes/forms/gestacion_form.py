from django import forms
from ..models import Gestacion


class GestacionForm(forms.ModelForm):
    class Meta:
        model = Gestacion
        exclude = ['created_by', 
                   'created_at', 
                   'updated_by', 
                   'updated_at', 
                   'fecha_inicio_gestacion']
        

    def clean(self):
        cleaned_data = super().clean()
        multiple = cleaned_data.get('multiple')
        n_fetos = cleaned_data.get('numero_fetos')

        # Datos asociados a como se obtuvieron las semanas de gestacion
        origen_datacion = cleaned_data.get('origen_datacion')
        fur = cleaned_data.get('fur')
        fecha_eco = cleaned_data.get('fecha_eco')
        semanas_eco = cleaned_data.get('semanas_eco')
        dias_eco = cleaned_data.get('dias_eco')

        if n_fetos is not None:
            if multiple and n_fetos <= 1:
                self.add_error('numero_fetos', 'Si es multiple la gestacion el número de fetos no puede ser menor o igual a 1')
            elif not multiple and n_fetos > 1:
                self.add_error('numero_fetos',  'No puede poner mas de un feto si no marca la gestacion como multiple')
        
        
        
        if origen_datacion == 'sin':
            if semanas_eco or dias_eco or fecha_eco or fur:
                self.add_error('origen_datacion', 'Si no marca el origen de la datacion no puede especificar "FECHA DEL FUR", "SEMANAS ECO", "DIAS ECO" ')
        elif origen_datacion == 'fur':
            if not fur:
                self.add_error('fur', "Si datacion es FUR debe especificar la fecha del FUR")
        elif origen_datacion == 'eco':
            if semanas_eco is None or dias_eco is None or fecha_eco is None:
                self.add_error('fecha_eco', 'Si la datacacion es por ECO debe especificar: "FECHA ECO", "SEMANAS ARROJADAS POR LA ECO", "DIAS ARROJADOS POR LA ECO"')
        return cleaned_data
            
        