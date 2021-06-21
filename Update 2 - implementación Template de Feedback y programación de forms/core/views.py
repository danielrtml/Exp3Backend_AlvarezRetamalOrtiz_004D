from django.shortcuts import render
from .models import Usuario

# Create your views here.

#metodos

def form_vehiculo(request):
    if request.method == 'POST': 
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()        #similar al insert de un modelo relacional 
            return redirect('home')
    else: 
        vehiculo_form = VehiculoForm()
    return render(request, 'core/form_crearvehiculo.html', {'vehiculo_form': vehiculo_form})

#Paginas
def Index(request):
    return render(request, 'index.html')

def contactenos(request):
    return render(request, 'contactenos.html')

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
