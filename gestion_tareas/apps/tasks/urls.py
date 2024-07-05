from django.urls import path

from .views import tasks

app_name='tasks'

urlpatterns = [
    path('', tasks, name='tasks_home'),
]