from django.shortcuts import render, redirect
from .models import PostDeComerciosForms, ProductosForms,ComercioForms,LocalidadesForms, CategoriaProductos
from UsuariosApp.models import ImgPerfil
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
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
        #imagen de perfil del usuario
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        # obtine el nombre del comercio
        comercio = PostDeComerciosForms.objects.filter(id=id)
        # ordena por categoria 
        categoria = CategoriaProductos.objects.filter(pertenece=id)
        print(categoria)
        # obtine los productos del comercio 
        form = ProductosForms.objects.filter(comercio_pertenece=id)
        
        return render(request, 'seccion_comercios.html',{'form':form, 'comer':comercio,'img':img_perfil,'cat':categoria})
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
    if request.method == 'POST':

        Subject = request.POST["Asunto"]
        message = request.POST["Mensaje"] + " " + request.POST["Email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["pruebaproyectof4@gmail.com"]
        send_mail (Subject, message, email_from, recipient_list)

        return render(request, 'mensaje.html')

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