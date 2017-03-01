from django.contrib import admin
from apps.categorias.models import Categoria

# Register your models here.
admin.site.register(Categoria)  # Esto activa en el admin el modelo indicado.
