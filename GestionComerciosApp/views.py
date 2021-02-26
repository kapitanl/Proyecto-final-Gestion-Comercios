from django.shortcuts import render
from django.template import Context
# Create your views here.


def home(request):
    return render(request, 'home.html')

def localidades(request):


    return render(request, 'localidades.html', )