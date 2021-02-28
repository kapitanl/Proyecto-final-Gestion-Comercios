from django.shortcuts import render, redirect
from .models import PostDeComerciosForms, ProductosForms
# Create your views here.


def home(request):
    form = PostDeComerciosForms.objects.all()
    return render(request, 'home.html',{'form':form})

def localidades(request):
    return render(request, 'localidades.html')

def seccionComercio(request, id):
    comercio = PostDeComerciosForms.objects.filter(id=id)
    form = ProductosForms.objects.filter(comercio_pertenece=id)
    return render(request, 'seccion_comercios.html',{'form':form, 'comer':comercio})
