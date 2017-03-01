# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarEditoriales, RegistrarEditorial, ActualizarEditorial, EliminarEditorial

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    url(r'^listar_editoriales/$', 'apps.editoriales.views.ListarEditoriales', name="listar_editoriales",),
    url(r'^registrar_editorial/', 'apps.editoriales.views.RegistrarEditorial', name="registrar_editorial",),
    url(r'^actualizar_editorial/(?P<pk>\d+)/$', 'apps.editoriales.views.ActualizarEditorial', name="actualizar_editorial",),
    url(r'^eliminar_editorial/(?P<pk>\d+)/$', 'apps.editoriales.views.EliminarEditorial', name="eliminar_editorial",),
    #url(r'^busqueda_ajax_centros/$','apps.registro.views.BuscarAjaxCentros', name='listar_centros',),
    #url(r'^busqueda_ajax2/$','apps.registro.views.BuscarAjaxPar', name='listar_municipios',),
    url(r'^data/', 'apps.editoriales.views.load_data', name="datos_editoriales",),  # URL de Importación para la data
]
