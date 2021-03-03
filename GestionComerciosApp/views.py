from django.shortcuts import render, redirect
from .models import PostDeComerciosForms, ProductosForms,ComercioForms,LocalidadesForms
from UsuariosApp.models import ImgPerfil
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        form = PostDeComerciosForms.objects.all()
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        return render(request, 'home.html',{'form':form,'img':img_perfil})
    else:
        form = PostDeComerciosForms.objects.all()
        return render(request, 'home.html',{'form':form})

def localidades(request):
    form = LocalidadesForms.objects.all()
    return render(request, 'localidades.html',{'formulario':form})

def seccionComercio(request, id):
    if request.user.is_authenticated:
        comercio = PostDeComerciosForms.objects.filter(id=id)
        form = ProductosForms.objects.filter(comercio_pertenece=id)
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        return render(request, 'seccion_comercios.html',{'form':form, 'comer':comercio,'img':img_perfil})
    else:
        comercio = PostDeComerciosForms.objects.filter(id=id)
        form = ProductosForms.objects.filter(comercio_pertenece=id)
        return render(request, 'seccion_comercios.html',{'form':form, 'comer':comercio})

def comercios(request):
    form = ComercioForms.objects.all()
    return render(request, 'comercios.html',{'form':form})

def info(request):
    return render(request, 'info.html') 

def contactanos(request):
    return render(request, 'contactanos.html')
