# -*- encoding: utf-8 -*-
from django.db import models
#from apps.topologia.estados.models import Estado
#from apps.topologia.municipios.models import Municipio
#from apps.topologia.parroquias.models import Parroquia
from apps.categorias.models import Categoria
from apps.autores.models import Autor
from apps.editoriales.models import Editorial
from apps.sedes.models import Sede
from apps.bitacora.models import Bitacora
from django.contrib.auth.models import User


class Libros(models.Model):
    """
    Clase para el mantenimiento de los libros:
    Registrar, Modificar, Eliminar y Consultar

    :param CharField cod_libro: campo donde se registra el código del libro.
    :param CharField titulo: campo donde se registra el título del libro.
    :param CharField autor: campo donde se registra el autor del libro.
    :param DateField fecha_pub: campo donde se registra la fecha de publicación del libro.
    :param CharField editorial: campo donde se registra la editorial del libro.
    :param CharField categoria: campo donde se registra la categoría del libro.
    :param CharField sede: campo donde se registra la sede de ubicación del libro.
    """
    cod_libro = models.CharField(verbose_name="Código de libro", unique=True, max_length=15, null=True, blank=True)
    titulo = models.CharField(verbose_name="Título", max_length=200, null=True, blank=True)
    autor = models.ForeignKey(Autor, to_field='cod_autor', on_delete=models.SET_NULL, related_name='autor_libro', null=True)
    fecha_pub = models.DateField(verbose_name="Fecha de Publicación", null=True, blank=True)
    editorial = models.ForeignKey(Editorial, to_field='cod_editorial', on_delete=models.SET_NULL, related_name='editorial_libro', null=True)
    categoria = models.ForeignKey(Categoria, to_field='cod_categoria', on_delete=models.SET_NULL, related_name='categoria_libro', null=True)
    sede = models.ForeignKey(Sede, to_field='cod_sede', on_delete=models.SET_NULL, related_name='sede_libro', null=True)
    #Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)

    def __unicode__(self):
        # Método para retornar por defecto el valor de un campo especificado
        return self.titulo
