from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

# Función para crear una cookie
from django.contrib.auth import login as login_django, logout as logout_django, authenticate
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

def logout(request):
    logout_django(request)
    return redirect('home')

def login(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        # Devuelve un usuario si es válido
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': "Usuario y/o contraseña incorrectos",
            })
        else:
            login_django(request, user)
            return redirect('tasks:tasks_home')








# ==============================================================================================







def helloword(request):
    # De la misma manera en que le mando un 'string'. También le puedo mandar un 'form'
    titulo = "Titulo de la página"
    ctx = {
        'titulo': titulo,
        'form': UserCreationForm()
    }
    return render(request, 'signup.html', context=ctx)