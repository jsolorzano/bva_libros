# -*- encoding: utf-8 -*-
from django.db import models
from apps.ejes.models import Eje
from apps.bitacora.models import Bitacora
from django.contrib.auth.models import User
# Create your models here.


class Sede(models.Model):
    """
    Clase para el mantenimiento de sedes:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField cod_area: campo donde se registra el código del área.
    :param ForeignKey cargo: campo de clave foránea donde se regitra el código del cargo asociado al área.
    :param CharField area: campo donde se registra el nombre del área.
    :param DateTimeField date_create: campo donde se registra la fecha y hora de creación del área.
    :param DateTimeField date_update: campo donde se registra la fecha y hora de actualización del área.
    :param CharField user: campo donde se registra el usuario que ha manipulado el módulo.
    """
    cod_sede = models.CharField(verbose_name="Código de sede", unique=True, max_length=15)
    eje = models.ForeignKey(Eje, to_field='cod_eje', on_delete=models.SET_NULL, related_name='eje_sede', null=True)
    sede = models.CharField(verbose_name="Sede", max_length=200)
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)

    def __unicode__(self):
        # Método para retornar por defecto el valor de un campo especificado
        return self.cod_sede
