from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'creditos']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del curso'
            }),
            'creditos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Créditos'
            }),
        }