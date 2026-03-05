from django.db import models
from universidad.Models.Alumno.models import Alumno
from asignacion_curso.models import AsignacionCurso


class Notas(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignacion = models.ForeignKey(AsignacionCurso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.alumno} - {self.asignacion} - {self.nota}"

    class Meta:
        db_table = 'notas'