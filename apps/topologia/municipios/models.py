# -*- encoding: utf-8 -*-
from django.db import models
from ..estados.models import Estado
from apps.circuitos.models import Circuitos
from apps.bitacora.models import Bitacora


class Municipio(models.Model):
    """
	Esta es la Clase que define todo lo referente a los estados
        Registrar Modificar Eliminar y Consultar
	
	:param CharField municipio: campo donde se registra el nombre del municipio.
	:param IntegerField cod_municipio: campo donde se registra el código del estado.
	:param ForeignKey estado: campo de clave foránea donde se regitra el código del estado asociado al municipio.
	:param ForeignKey circuito: campo de clave foránea donde se regitra el código del circuito asociado al municipio.
	:param DateTimeField date_create: campo donde se registra la fecha y hora de creación del municipio.
	:param DateTimeField date_update: campo donde se registra la fecha y hora de actualización del municipio.
	:param CharField user: campo donde se registra el usuario que ha manipulado el módulo.
    """
    municipio = models.CharField(verbose_name="Municipio", max_length=50)
    cod_municipio = models.IntegerField(null=True)
    estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='estado_municipio', null=True) # Clave unica que hace referencia a estado a traves de cod_estado con clave unica (unique)
    circuito = models.ForeignKey(Circuitos, to_field='codigo', on_delete=models.SET_NULL, related_name='circuito_municipio', null=True)
    date_create = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    date_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    user = models.CharField(max_length=15, null=True)

    def __unicode__(self):
        return self.municipio
