from django import forms
from .models import Catedratico

class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del catedrático'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
        }