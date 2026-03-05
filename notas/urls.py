from django.urls import path
from . import views

urlpatterns = [
    path('', views.notas_list, name='notas_list'),
    path('crear/', views.notas_create, name='notas_create'),
    path('<int:pk>/editar/', views.notas_edit, name='notas_edit'),
    path('<int:pk>/eliminar/', views.notas_delete, name='notas_delete'),
]