from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

#metodos

#Paginas
def Index(request):
    return render(request, 'index.html')

def contactenos(request):
    if request.method == 'POST': 
        usuario = UsuarioForm(request.POST)
        if usuario.is_valid():
            usuario.save()        #similar al insert de un modelo relacional 
            return redirect('Index')
    else: 
        usuario = UsuarioForm()
    return render(request, 'core/contactenos.html', {'usuario': usuario})

def galeria(request):
    return render(request, 'galeria.html')

def api(request):
    return render(request, 'api.html')

def registro(request):
    return render(request, 'registro.html')

def whorwe(request):
    return render(request, 'who-r-we.html')

def inise(request):
    return render(request, 'ini-se.html')

def news(request):
    return render(request, 'news.html')

def feedback(request):
    usuario=Usuario.objects.all()
    return render(request, 'feedback.html', context={'usuarios':usuario})

def mod_feedback(request, id):
    usuario= Usuario.objects.get(NickUsuario=id)

    datos ={
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance = usuario)
        if formulario.is_valid:
            formulario.save()
            return redirect('feedback')
    return render(request, 'core/mod_feedback.html', datos)