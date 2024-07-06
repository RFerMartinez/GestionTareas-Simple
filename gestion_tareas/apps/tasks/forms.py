from django.forms import ModelForm

from .models import Task

class TaskForm(ModelForm):

    # Aquí le indico sobre qué modelo se estará basando el formulario
    class Meta:
        model = Task # El modelo a utilizar
        fields = ['titulo', 'descripcion', 'importante'] # Los campos que se mostrarán en el frontend
