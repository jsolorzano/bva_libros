from django.forms import ModelForm
from django import forms
from apps.autores.models import Autor


class FormAutores(ModelForm):
    class Meta:
        model = Autor
        exclude = {'user', }
