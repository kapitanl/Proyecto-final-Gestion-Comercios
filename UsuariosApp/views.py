from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as to_login
from django.contrib.auth import logout as to_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

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
    return redirect('/')


def perfil(request):
    if request.user.is_authenticated:
        return render(request, 'perfil.html')
    else:
        return redirect('login')