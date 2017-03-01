# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarCategorias, RegistrarCategoria, ActualizarCategoria, EliminarCategoria

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    url(r'^listar_categorias/$', 'apps.categorias.views.ListarCategorias', name="listar_categorias",),
    url(r'^registrar_categoria/', 'apps.categorias.views.RegistrarCategoria', name="registrar_categoria",),
    url(r'^actualizar_categoria/(?P<pk>\d+)/$', 'apps.categorias.views.ActualizarCategoria', name="actualizar_categoria",),
    url(r'^eliminar_categoria/(?P<pk>\d+)/$', 'apps.categorias.views.EliminarCategoria', name="eliminar_categoria",),
    #url(r'^busqueda_ajax_centros/$','apps.registro.views.BuscarAjaxCentros', name='listar_centros',),
    #url(r'^busqueda_ajax2/$','apps.registro.views.BuscarAjaxPar', name='listar_municipios',),
    url(r'^data/', 'apps.categorias.views.load_data', name="datos_categorias",),  # URL de Importación para la data
]
