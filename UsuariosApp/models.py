from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ImgPerfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    img_perfil = models.ImageField(upload_to='imgPerfil')

    

