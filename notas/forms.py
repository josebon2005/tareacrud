from django import forms
from .models import Notas


class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['alumno', 'asignacion', 'nota']