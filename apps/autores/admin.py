from django.contrib import admin
from apps.autores.models import Autor

# Register your models here.
admin.site.register(Autor)  # Esto activa en el admin el modelo indicado.
