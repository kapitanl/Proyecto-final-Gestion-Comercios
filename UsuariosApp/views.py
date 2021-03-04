from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as to_login
from django.contrib.auth import logout as to_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import ImgPerfil
from .forms import ImgPerfilFormulario

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
        img_perfil = ImgPerfil.objects.filter(usuario=request.user)
        return render(request, 'perfil.html',{'img':img_perfil})
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
