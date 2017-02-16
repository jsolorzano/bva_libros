# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarAutores, RegistrarAutor, ActualizarAutor, EliminarAutor

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    url(r'^listar_autores/$', 'apps.autores.views.ListarAutores', name="listar_autores",),
    url(r'^registrar_autor/', 'apps.autores.views.RegistrarAutor', name="registrar_autor",),
    url(r'^actualizar_autor/(?P<pk>\d+)/$', 'apps.autores.views.ActualizarAutor', name="actualizar_autor",),
    url(r'^eliminar_autor/(?P<pk>\d+)/$', 'apps.autores.views.EliminarAutor', name="eliminar_autor",),
    #url(r'^busqueda_ajax_centros/$','apps.registro.views.BuscarAjaxCentros', name='listar_centros',),
    #url(r'^busqueda_ajax2/$','apps.registro.views.BuscarAjaxPar', name='listar_municipios',),
    url(r'^data/', 'apps.autores.views.load_data', name="datos_autores",),  # URL de Importación para la data
]
