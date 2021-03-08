from django.shortcuts import render, redirect
from .models import PostDeComerciosForms, ProductosForms,ComercioForms,LocalidadesForms, CategoriaProductos
from UsuariosApp.models import ImgPerfil
from django.db.models import Count

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
    # obtiene todas las localidades
    all_localidades = LocalidadesForms.objects.all()
    # obtiene todas los post para comparar la localidad
    all_post= PostDeComerciosForms.objects.values("localidad_id").distinct()

    return render(request, 'localidades.html',{'localidades':all_localidades,'post':all_post})

def seccionComercio(request, id):
    if request.user.is_authenticated:
        #imagen de perfil del usuario
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        # obtine el nombre del comercio
        comercio = PostDeComerciosForms.objects.filter(id=id)
        # obtine los productos del comercio 
        form = ProductosForms.objects.filter(comercio_pertenece=id)
        
        return render(request, 'seccion_comercios.html',{'form':form, 'comer':comercio,'img':img_perfil})
    else:
        comercio = PostDeComerciosForms.objects.filter(id=id)
        form = ProductosForms.objects.filter(comercio_pertenece=id)
        return render(request, 'seccion_comercios.html',{'form':form, 'comer':comercio})

def comercios(request):
    # obtiene  los distintos comercios que hay
    all_comercio = ComercioForms.objects.all()
    # obtiene todas los post para comparar con comercios 
    all_post= PostDeComerciosForms.objects.values("tipo_comercio_id").distinct()
    return render(request, 'comercios.html',{'comercio':all_comercio,'post':all_post})

def info(request):
    return render(request, 'info.html') 

def contactanos(request):
    return render(request, 'contactanos.html')

def categoriaDeProductos(request, id):
    if request.user.is_authenticated:
        # imagen de perfil del usuario 
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)

        # muestra lo que tine la categoria 
        lista = CategoriaProductos.objects.filter(id=id)
        return render(request, 'categorias.html',{'img':img_perfil, 'lista':lista})
    else:
        return render(request, 'categorias.html',)

def por_localidad(request, id):
    # lista los comercio que hay en esa localidad
    comercio = PostDeComerciosForms.objects.filter(localidad_id=id)
    return render(request, 'por_localidad.html',{'comercios':comercio})

def por_comercio(request, id):
    # lista los comercio que hay en esa localidad
    comercio = PostDeComerciosForms.objects.filter(tipo_comercio_id=id)
    return render(request, 'por_comercio.html',{'comercios':comercio})