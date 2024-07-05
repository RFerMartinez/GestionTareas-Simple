from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

# Función para crear una cookie
from django.contrib.auth import login as login_django
# Estas cooki me van a servir para obtener los datos del usuario, para saber si 'x tarea' fue
# creada por ese usuario, o si el usuario tiene acceso a determinadas páginas

from django.db import IntegrityError

def home(request):
    return render(request, 'home.html')

# Función para enviar el archivo que va a contener el formulario
def signup(request):

    if request.method == 'GET':
        print("enviando formulario")
        ctx = {
        'form': UserCreationForm(),
        }
        return render(request, 'signup.html', context=ctx)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login_django(request, user)
                # return HttpResponse("Usuario creado correctamente")
                return redirect('tasks:tasks_home')
            except IntegrityError:
                return render(request, 'signup.html',  {
                    'form': UserCreationForm(),
                    'error': "Usuario ya existe",
                })
        return render(request, 'signup.html',  {
            'form': UserCreationForm(),
            'error': "Las contraseñas no coinciden",
        })

def tasks(request):
    return render(request, 'tasks/tasks.html')
    







# ==============================================================================================







def helloword(request):
    # De la misma manera en que le mando un 'string'. También le puedo mandar un 'form'
    titulo = "Titulo de la página"
    ctx = {
        'titulo': titulo,
        'form': UserCreationForm()
    }
    return render(request, 'signup.html', context=ctx)