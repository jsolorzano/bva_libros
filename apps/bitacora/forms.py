from django.forms import ModelForm
from django import forms
from apps.bitacora.models import Bitacora


class FormBitacora(ModelForm):
    class Meta:
        model = Bitacora
        exclude = {'user', }
