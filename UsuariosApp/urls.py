from django.urls import path
from UsuariosApp.views import  login, registro, logout, perfil


urlpatterns = [
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', logout, name='logout'),
    path('perfil/',perfil , name='perfil'),
]