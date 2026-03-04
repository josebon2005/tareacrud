from django import forms
from .models import AsignacionCurso

class AsignacionCursoForm(forms.ModelForm):
    class Meta:
        model = AsignacionCurso
        fields = ['curso', 'catedratico', 'horario']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'catedratico': forms.Select(attrs={'class': 'form-select'}),
            'horario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Lunes y Miércoles 08:00-10:00'
            }),
        }