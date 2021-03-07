from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as to_login
from django.contrib.auth import logout as to_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import ImgPerfil
from .forms import ImgPerfilFormulario, PostDeComerciosFormulario, ProductosFormulario
from GestionComerciosApp.models import PostDeComerciosForms, ProductosForms

# Create your views here.


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            
            if user is not None:
                to_login(request, user)
                return redirect('/')


    return render(request, 'login.html', {'form': form})

def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            
            if user is not None:
                to_login(request, user)
                return redirect('/')
    return render(request, 'registro.html', {'form': form})

def logout(request):
    to_logout(request)
    return redirect('home')


def perfil(request):
    if request.user.is_authenticated:
        # imagen de perfil 
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        # enlita los comercios del usuario
        com_list = PostDeComerciosForms.objects.filter(post_user=request.user)
        # muestran los productos que se van agregando 
        productos = ProductosForms.objects.all()
        return render(request, 'perfil.html',{'img':img_perfil, 'comercios':com_list,'productos':productos})
    else:
        return redirect('login')


def editar_perfil(request):
    if request.user.is_authenticated:
        if ImgPerfil.objects.filter(usuario=request.user).exists():
            img_perfil = ImgPerfil.objects.get(usuario=request.user)
            form = ImgPerfilFormulario(instance=img_perfil)
            if request.method == 'POST':
                form = ImgPerfilFormulario(data=request.POST, instance=img_perfil, files=request.FILES)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.usuario= request.user
                    user.save()
                    form = ImgPerfilFormulario(instance=img_perfil)
        else:
            img_perfil = ImgPerfil.objects.filter(usuario=request.user)
            form = ImgPerfilFormulario()
            if request.method == 'POST':
                form = ImgPerfilFormulario(data=request.POST, files=request.FILES)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.usuario = request.user
                    user.save()
                    return redirect('editar_perfil')
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)    
        return render(request, 'editarPerfil.html',{'form':form,'img':img_perfil})
    else:
        return redirect('login')


def add_comercio(request):
    if request.user.is_authenticated:
        # imagen de perfil 
        img_perfil = ImgPerfil.objects.filter(usuario=request.user) 

        # fomrulario para publicar
        form = PostDeComerciosFormulario()
        if request.method == 'POST':
            form = PostDeComerciosFormulario(data=request.POST, files=request.FILES)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.post_user = request.user
                usuario.save()
                return redirect('perfil')
        return render(request, 'add_comercio.html',{'img':img_perfil, 'form':form})
    else:
        return redirect('login')

def editar_comercio(request, id):
    if request.user.is_authenticated:
        # imagen de perfil 
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        
        # obter el post para editarlo
        get_post = PostDeComerciosForms.objects.get(id=id)
        form = PostDeComerciosFormulario(instance=get_post)
        if request.method == 'POST':
            form = PostDeComerciosFormulario(data=request.POST, instance=get_post, files=request.FILES)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.post_user = request.user
                usuario.save()
                form = PostDeComerciosFormulario(instance=get_post)

        return render(request, 'editar_comercio.html',{'img':img_perfil, 'form':form})
    else:
        return redirect('login')


def eliminar_comercio(request, id):
    comercio = PostDeComerciosForms.objects.get(id=id)
    comercio.delete()
    return redirect('perfil')

def add_productos(request, id):
    if request.user.is_authenticated:
        # imagen de perfil 
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        # formulario para agreagar productos 
        form = ProductosFormulario()
        if request.method == 'POST':
            form = ProductosFormulario(data=request.POST, files=request.FILES)
            if form.is_valid():
                comercio = form.save(commit=False)
                comercio.comercio_pertenece_id = id
                comercio.save()
                return redirect('perfil')
        return render(request, 'add_productos.html',{'img':img_perfil, 'form':form})
    else:
        return redirect('login')