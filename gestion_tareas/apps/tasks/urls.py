from django.urls import path

from . import views

app_name='tasks'

urlpatterns = [
    path('', views.tasks, name='tasks_home'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('detalle_tarea/<int:id_de_tarea>', views.detalle_tarea, name='detalle_tarea'),
]