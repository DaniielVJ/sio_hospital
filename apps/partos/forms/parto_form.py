from django import forms
from ..models import Parto


class PartoForm(forms.ModelForm):
    class Meta:
        model = Parto
        exclude = [
            'created_by', 'created_at', 'updated_by', 'updated_at',
            'edad_madre'
            ]
        
