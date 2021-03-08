from django import forms
from .models import ImgPerfil
from GestionComerciosApp.models import PostDeComerciosForms, ProductosForms, CategoriaProductos

class ImgPerfilFormulario(forms.ModelForm):

    class Meta:
        model = ImgPerfil
        fields = [
                'img_perfil',
        ]


class PostDeComerciosFormulario(forms.ModelForm):

    class Meta:
        model = PostDeComerciosForms
        fields = [
                'nombre_del_comercio', 'tipo_comercio', 'descripcion', 'img_comercio','localidad',
        ]

class ProductosFormulario(forms.ModelForm):

        class Meta:
                model = ProductosForms
                fields = [
                        'nombre_producto','precio_producto','img_producto',
                ]

class CategoriaProductosFormulario(forms.ModelForm):

        class Meta:
                model = CategoriaProductos
                fields = [
                        'nom_categoria_productos',
                ]