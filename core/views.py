from django.shortcuts import render

# Create your views here.
def inicio(request):
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