from django import forms



class MotivoEliminacionForm(forms.Form):
    motivo = forms.CharField(max_length=150, widget=forms.Textarea(
        attrs={
            "placeholder": "Indique la razon de eliminacion del registro"
        }
    ), required=True)