from django.forms import ModelForm
from django import forms
from apps.categorias.models import Categoria


class FormCategorias(ModelForm):
    class Meta:
        model = Categoria
        exclude = {'user', }
