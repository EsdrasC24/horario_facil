from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_horarios, name='lista_horarios'),
    path('crear/', views.crear_horario, name='crear_horario'),
    path('<int:id>/', views.detalle_horario, name='detalle_horario'),
    path('<int:id>/editar/', views.editar_horario, name='editar_horario'),
    path('<int:id>/eliminar/', views.eliminar_horario, name='eliminar_horario'),
]
