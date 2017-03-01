# -*- encoding: utf-8 -*-
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from ..estados.models import Estado
from ..municipios.models import Municipio
from apps.bitacora.models import Bitacora


class Parroquia(models.Model):
	"""
	Esta es la Clase que define todo lo referente a los parroquias
	Registrar Modificar Eliminar y Consultar
	
	:param CharField parroquia: campo donde se registra el nombre de la parroquia.
	:param ForeignKey estado: campo donde se registra el código del estado.
	:param IntegerField cod_parroquia: campo donde se registra el código de la parroquia.
	:param IntegerField municipio: campo donde se registra el código del municipio.
	:param DateTimeField date_create: campo donde se registra la fecha y hora de creación del parroquia.
	:param DateTimeField date_update: campo donde se registra la fecha y hora de actualización del parroquia.
	:param CharField user: campo donde se registra el usuario que ha manipulado el módulo.
	"""
	parroquia = models.CharField(max_length=50)
	estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='estado_parroquia', null=True)
	cod_parroquia = models.IntegerField(null=True)
	municipio = models.IntegerField(null=True)
	date_create = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	date_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	user = models.CharField(max_length=15, null=True)

	def __unicode__(self):
		return self.parroquia

	def __str__(self):
		return self.parroquia
