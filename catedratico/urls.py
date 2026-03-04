from django.urls import path
from . import views

app_name = 'catedratico'

urlpatterns = [
    path('', views.catedratico_list, name='list'),
    path('crear/', views.catedratico_create, name='create'),
    path('<int:pk>/', views.catedratico_detail, name='detail'),
    path('<int:pk>/editar/', views.catedratico_edit, name='edit'),
    path('<int:pk>/eliminar/', views.catedratico_delete, name='delete'),
]