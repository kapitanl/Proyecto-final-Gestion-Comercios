from django.db import models

# Create your models here.

class LocalidadesForms(models.Model):
    localidad = models.CharField(max_length=200)

    def __str__(self):
        return self.localidad

class ComercioForms(models.Model):
    comercio = models.CharField(max_length=150)

    def __str__(self):
        return self.comercio

class PostDeComerciosForms(models.Model):
    nombre_del_comercio = models.CharField(max_length=100)
    tipo_comercio = models.ForeignKey(ComercioForms, on_delete=models.CASCADE)
    descripcion = models.TextField()
    img_comercio = models.ImageField(upload_to='comercos')
    localidad = models.ForeignKey(LocalidadesForms,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_del_comercio

