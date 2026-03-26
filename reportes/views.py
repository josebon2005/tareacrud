from django.shortcuts import render
from django.db.models import Count
from inscripcion_alumno.models import InscripcionAlumno
from asignacion_curso.models import AsignacionCurso


def reporte_alumnos_cursos(request):
    inscripciones = InscripcionAlumno.objects.select_related(
        'alumno',
        'asignacion',
        'asignacion__curso',
        'asignacion__catedratico'
    ).all()

    return render(request, 'reportes/reporte_alumnos_cursos.html', {
        'inscripciones': inscripciones
    })


def reporte_cursos_inscritos(request):
    asignaciones = AsignacionCurso.objects.select_related(
        'curso',
        'catedratico'
    ).annotate(
        total_inscritos=Count('inscripcionalumno')
    )

    return render(request, 'reportes/reporte_cursos_inscritos.html', {
        'asignaciones': asignaciones
    })