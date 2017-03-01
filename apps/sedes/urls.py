# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarSedes, RegistrarSede, ActualizarSede, EliminarSede

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    url(r'^listar_sedes/$', 'apps.sedes.views.ListarSedes', name="listar_sedes",),
    url(r'^registrar_sede/', 'apps.sedes.views.RegistrarSede', name="registrar_sede",),
    url(r'^actualizar_sede/(?P<pk>\d+)/$', 'apps.sedes.views.ActualizarSede', name="actualizar_sede",),
    url(r'^eliminar_sede/(?P<pk>\d+)/$', 'apps.sedes.views.EliminarSede', name="eliminar_sede",),
    #url(r'^busqueda_ajax_centros/$','apps.registro.views.BuscarAjaxCentros', name='listar_centros',),
    #url(r'^busqueda_ajax2/$','apps.registro.views.BuscarAjaxPar', name='listar_municipios',),
    url(r'^data/', 'apps.sedes.views.load_data', name="datos_sedes",),  # URL de Importación para la data
]
