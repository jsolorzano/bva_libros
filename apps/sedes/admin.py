from django.contrib import admin
from apps.sedes.models import Sede

# Register your models here.
admin.site.register(Sede)  # Esto activa en el admin el modelo indicado.
