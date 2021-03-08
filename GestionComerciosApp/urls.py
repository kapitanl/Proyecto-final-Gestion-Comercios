from django.urls import path
from .views import home, localidades, seccionComercio, info, contactanos,comercios, categoriaDeProductos, por_comercio, por_localidad
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
    path('Localidades',localidades, name='localidades'),
    path('seccionComercio<int:id>',seccionComercio, name='seccionComercio'),
    path('info',info, name='info'),
    path('contactanos',contactanos, name='contactanos'),
    path('comercios',comercios, name='comercios'),
    path('categoriaDeProductos<int:id>',categoriaDeProductos, name='categoriaDeProductos'),
    path('por_localidad/<int:id>',por_localidad, name='por_localidad'),
    path('por_comercio/<int:id>',por_comercio, name='por_comercio'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)