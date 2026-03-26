from django.urls import path
from . import views

urlpatterns = [
    path('reporte-alumnos-cursos/', views.reporte_alumnos_cursos, name='reporte_alumnos_cursos'),
    path('reporte-cursos-inscritos/', views.reporte_cursos_inscritos, name='reporte_cursos_inscritos'),
]