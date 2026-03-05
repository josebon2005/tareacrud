from django import forms
from .models import InscripcionAlumno


class InscripcionAlumnoForm(forms.ModelForm):
    class Meta:
        model = InscripcionAlumno
        fields = ['alumno', 'asignacion', 'fecha_asignacion']