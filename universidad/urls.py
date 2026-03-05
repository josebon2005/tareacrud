from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('', core_views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),

    path('alumnos/', include('universidad.Models.Alumno.urls')),
    path('cursos/', include('curso.urls')),
    path('catedraticos/', include('catedratico.urls')),
    path('asignaciones/', include('asignacion_curso.urls')),
    path('inscripciones/', include('inscripcion_alumno.urls')),
    path('notas/', include('notas.urls')),
]