from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_asignaturas, name='lista_asignaturas'),
    path('crear/', views.crear_asignatura, name='crear_asignatura'),
    path('<int:id>/', views.detalle_asignatura, name='detalle_asignatura'),
    path('<int:id>/editar/', views.editar_asignatura, name='editar_asignatura'),
    path('<int:id>/eliminar/', views.eliminar_asignatura, name='eliminar_asignatura'),
]
