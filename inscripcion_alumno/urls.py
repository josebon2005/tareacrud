from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscripcion_list, name='inscripcion_list'),
    path('crear/', views.inscripcion_create, name='inscripcion_create'),
    path('<int:pk>/editar/', views.inscripcion_edit, name='inscripcion_edit'),
    path('<int:pk>/eliminar/', views.inscripcion_delete, name='inscripcion_delete'),
]