from django.forms import ModelForm
from django import forms
from apps.sedes.models import Sede


class FormSedes(ModelForm):
    class Meta:
        model = Sede
        exclude = {'user', }
