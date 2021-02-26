from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import localidades

urlpatterns = [
    path('',home, name='home'),
    path('Localidades',localidades, name='Localidades'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)