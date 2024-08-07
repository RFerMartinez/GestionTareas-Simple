from django.urls import path

from . import views

app_name='tasks'

urlpatterns = [
    path('', views.tasks, name='tasks_home'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('detalle_tarea/<int:id_de_tarea>', views.detalle_tarea, name='detalle_tarea'),
    path('detalle_tarea/<int:id_de_tarea>/completada', views.completar_tarea, name='completar_tarea'),
    path('detalle_tarea/<int:id_de_tarea>/borrar', views.borrar_tarea, name='borrar_tarea'),
    path('completadas', views.tareas_completadas, name='tareas_completadas'),
]