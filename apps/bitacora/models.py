# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.


class Bitacora(models.Model):
    """
    Clase para el mantenimiento de la Bitacora:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField accion: campo que contiene la acción realizada.
    :param CharField usuario: campo que contiene el usuario que realizó la acción
    :param DateTimeField fecha: campo que contiene la fecha y hora en que se realizó la acción.
    """
    accion = models.CharField(verbose_name="Acción", max_length=200)
    usuario = models.CharField(verbose_name="Cargo", max_length=50)
    fecha = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        # Método para retornar por defecto el valor de un campo especificado
        return self.accion
