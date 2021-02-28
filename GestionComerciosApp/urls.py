from django.urls import path
from .views import home, localidades, info, contactanos, comercios 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
    path('Localidades',localidades, name='localidades'),
    path('info',info, name='info'),
    path('contactanos',contactanos, name='contactanos'),
    path('comercios',comercios, name='comercios'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)