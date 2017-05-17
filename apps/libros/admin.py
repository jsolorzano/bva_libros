from django.contrib import admin
from apps.libros.models import Libros

# Register your models here.
admin.site.register(Libros)  # Esto activa en el admin el modelo indicado.
