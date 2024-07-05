from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

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
                return HttpResponse("Usuario creado correctamente")
            except:
                return HttpResponse('username ya existe')
        return HttpResponse('Las contraseñas no coinciden')

    







# ==============================================================================================







def helloword(request):
    # De la misma manera en que le mando un 'string'. También le puedo mandar un 'form'
    titulo = "Titulo de la página"
    ctx = {
        'titulo': titulo,
        'form': UserCreationForm()
    }
    return render(request, 'signup.html', context=ctx)