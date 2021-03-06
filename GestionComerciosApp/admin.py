from django.contrib import admin
from .models import PostDeComerciosForms, LocalidadesForms, ComercioForms, ProductosForms, CategoriaProductos
# Register your models here.
admin.site.register(PostDeComerciosForms)
admin.site.register(LocalidadesForms)
admin.site.register(ComercioForms)
admin.site.register(ProductosForms)
admin.site.register(CategoriaProductos)