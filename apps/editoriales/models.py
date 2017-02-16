# -*- encoding: utf-8 -*-
from django.db import models
from apps.bitacora.models import Bitacora
from django.contrib.auth.models import User

# Create your models here.


class Editorial(models.Model):
    """
    Clase para el mantenimiento de categorías:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField cod_categoria: campo donde se crea el código de la editorial.
    :param CharField categoria: campo donde se registra el nombre de la editorial.
    :param DateTimeField date_create: campo donde se registra la fecha de creación de la categoría.
    :param DateTimeField date_update: campo donde se registra la fecha de actualización de la categoría.
    :param CharField user: campo donde se registra el usuario que ha manipulado el módulo.
    """
    cod_editorial = models.CharField(verbose_name="Código de la editorial", unique=True, max_length=15)
    editorial = models.CharField(verbose_name="Editorial", max_length=200)
    #Auditoría
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)

    def __unicode__(self):
        # Método para retornar por defecto el valor de un campo especificado
        return self.cod_editorial
