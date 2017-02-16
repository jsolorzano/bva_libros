from django.forms import ModelForm
from django import forms
from apps.libros.models import Libros


class FormLibros(ModelForm):
    class Meta:
        model = Libros
        exclude = {'user', }
