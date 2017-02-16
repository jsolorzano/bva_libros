from django.forms import ModelForm
from django import forms
from apps.ejes.models import Eje


class FormEjes(ModelForm):
    class Meta:
        model = Eje
        exclude = {'user', }
