# -*- encoding: utf-8 -*-
from django.db import models
from apps.bitacora.models import Bitacora
from django.contrib.auth.models import User
# Create your models here.


class Eje(models.Model):
    """
    Clase para el mantenimiento de ejes:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField cod_eje: campo donde se crea el código del cargo.
    :param CharField eje: campo donde se registra el nombre del cargo.
    :param DateTimeField date_create: campo donde se registra la fecha de creación del cargo.
    :param DateTimeField date_update: campo donde se registra la fecha de actualización del cargo.
    :param CharField user: campo donde se registra el usuario que ha manipulado el módulo.
    """
    cod_eje = models.CharField(verbose_name="Código del eje", unique=True, max_length=15)
    eje = models.CharField(verbose_name="Eje", max_length=200)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)

    def __unicode__(self):
        # Método para retornar por defecto el valor de un campo especificado
        return self.cod_eje
