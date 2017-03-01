from django.forms import ModelForm
from django import forms
from apps.editoriales.models import Editorial


class FormEditoriales(ModelForm):
    class Meta:
        model = Editorial
        exclude = {'user', }
