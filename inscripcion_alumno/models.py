from django.db import models

from universidad.Models.Alumno.models import Alumno
from asignacion_curso.models import AsignacionCurso


class InscripcionAlumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignacion = models.ForeignKey(AsignacionCurso, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()

    def __str__(self):
        return f"{self.alumno} -> {self.asignacion}"

    class Meta:
        db_table = 'inscripcion_alumno'