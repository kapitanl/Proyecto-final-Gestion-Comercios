from django.shortcuts import render, redirect
from .models import ComercioForms,PostDeComerciosForms

# Create your views here.


def home(request):
    return render(request, 'home.html')

def localidades(request):
    return render(request, 'localidades.html')

def comercios(request):
    form = ComercioForms.objects.all()
    return render(request, 'comercios.html',{'form':form})

def info(request):
    return render(request, 'info.html') 

def contactanos(request):
    return render(request, 'contactanos.html')