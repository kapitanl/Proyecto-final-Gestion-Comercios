from django.urls import path
from .views import home, localidades 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='home'),
    path('Localidades',localidades, name='localidades')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)