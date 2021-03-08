from django.urls import path
from UsuariosApp.views import  login, registro, logout, perfil, editar_perfil, add_comercio, editar_comercio,eliminar_comercio, add_productos, add_categoria


urlpatterns = [
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', logout, name='logout'),
    path('perfil/',perfil , name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('add_comercio/',add_comercio , name='add_comercio'),
    path('editar_comercio/<int:id>',editar_comercio , name='editar_comercio'),
    path('eliminar_comercio/<int:id>', eliminar_comercio, name='eliminar_comercio'),
    path('add_productos/<int:id>',add_productos , name='add_productos'),
    path('add_categoria',add_categoria , name='add_categoria'),
]