from django import forms


class FormulariosDeContactos(forms.Form):

    asunto= forms.CharField()
    email= forms.EmailField()
    mensaje= forms.CharField()