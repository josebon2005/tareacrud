from django.urls import path
from . import views

app_name = 'asignacion'

urlpatterns = [
    path('', views.asignacion_list, name='list'),
    path('crear/', views.asignacion_create, name='create'),
    path('<int:pk>/editar/', views.asignacion_edit, name='edit'),
    path('<int:pk>/eliminar/', views.asignacion_delete, name='delete'),
]