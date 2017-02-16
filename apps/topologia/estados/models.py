# -*- encoding: utf-8 -*-
from django.db import models
from apps.bitacora.models import Bitacora

# Esta es mi CLASE.


class Estado(models.Model):
    """
	Esta es la Clase que define todo lo referente a los estados
        Registrar Modificar Eliminar y Consultar
	
	:param CharField cod_estado: campo donde se registra el código del estado.
	:param CharField estado: campo donde se registra el nombre del estado.
	:param DateTimeField date_create: campo donde se registra la fecha y hora de creación del estado.
	:param DateTimeField date_update: campo donde se registra la fecha y hora de actualización del estado.
	:param CharField user: campo donde se registra el usuario que ha manipulado el módulo.
    """
    cod_estado = models.IntegerField(unique=True)
    estado = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    date_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    user = models.CharField(max_length=15, null=True, blank=True)
    
    

    def __unicode__(self):
        return self.estado
