from django import forms
from .models import ImgPerfil

class ImgPerfilFormulario(forms.ModelForm):

    class Meta:
        model = ImgPerfil
        fields = [
                'img_perfil',
        ]