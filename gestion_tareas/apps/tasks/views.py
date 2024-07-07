from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Función para crear una cookie
from django.contrib.auth import login as login_django, logout as logout_django, authenticate
# Estas cooki me van a servir para obtener los datos del usuario, para saber si 'x tarea' fue
# creada por ese usuario, o si el usuario tiene acceso a determinadas páginas

from django.db import IntegrityError
from django.utils import timezone

# Importar el formulario de Task
from .forms import TaskForm

from .models import Task

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

@login_required
def tasks(request):
    # Filtro las tareas por el usuario que hace el request, y filtro por aquellas tareas que no tengan fecha de completado
    tareas = Task.objects.filter(user=request.user, fecha_completado__isnull=True)
    ctx = {
        'tareas': tareas
    }
    return render(request, 'tasks/tasks.html', ctx)

@login_required
def tareas_completadas(request):
    tareas_completadas = Task.objects.filter(user=request.user, fecha_completado__isnull=False)
    print(type(tareas_completadas))
    print(tareas_completadas.count())
    cantidad = tareas_completadas.count()
    ctx = {
        'tareas_comlpetadas': tareas_completadas,
        'cantidad': cantidad,
    }
    return render(request, 'tasks/tareas_completadas.html', ctx)

@login_required
def detalle_tarea(request, id_de_tarea):
    if request.method == 'GET':
        # tarea = Task.objects.get(id=id_de_tarea)
        tarea = get_object_or_404(Task, id=id_de_tarea, user=request.user)

        form = TaskForm(instance=tarea)
        ctx = {
            'id_tarea': id_de_tarea,
            'tarea': tarea,
            'form':form,
        }
        return render(request, 'tasks/detalle_de_tarea.html', ctx)
    else:
        try:
            tarea = get_object_or_404(Task, id=id_de_tarea, user=request.user)
            form = TaskForm(request.POST, instance=tarea) # 'instance=tarea' quiere decir que rellena el form con los datos de la tarea para poder actualizarlos
            form.save()
            return redirect('tasks:tasks_home')
        except ValueError:
            return HttpResponse("Error")

@login_required
def completar_tarea(request, id_de_tarea):
    # Primeramente hay que buscar una tarea
    tarea = get_object_or_404(Task, id=id_de_tarea, user=request.user)

    # operacion/lógica con la tarea
    if request.method == 'POST':
        # agregarle una fecha de completado
        tarea.fecha_completado = timezone.now()
        #guardar tarea
        tarea.save()
        return redirect('tasks:tasks_home')

@login_required
def borrar_tarea(request, id_de_tarea):
    # Primeramente hay que buscar una tarea
    tarea = get_object_or_404(Task, id=id_de_tarea, user=request.user)

    # operacion/lógica con la tarea
    if request.method == 'POST':
        # eliminar la tarea encontrada
        tarea.delete()
        return redirect('tasks:tasks_home')

@login_required
def crear_tarea(request):
    if request.method == 'GET':
        ctx = {
            'form': TaskForm
        }
        return render(request, 'tasks/crear_tarea.html', ctx)
    else:
        try:
            # GUARDAR LOS DATOS
            # print(request.POST)
            form = TaskForm(request.POST) # devuelve un html (o crea un formulario) con los datos ingresados desde el front
            print(form)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            
            print(nueva_tarea)
            return redirect('tasks:tasks_home')
        except:
            ctx = {
            'form': TaskForm,
            'error': "ingresa los datos correcto"
            }
            return render(request, 'tasks/crear_tarea.html', ctx)

@login_required
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