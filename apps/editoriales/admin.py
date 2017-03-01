from django.contrib import admin
from apps.editoriales.models import Editorial

# Register your models here.
admin.site.register(Editorial)  # Esto activa en el admin el modelo indicado.
