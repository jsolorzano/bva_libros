# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarEjes, RegistrarEje, ActualizarEje, EliminarEje

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    url(r'^listar_ejes/$', 'apps.ejes.views.ListarEjes', name="listar_ejes",),
    url(r'^registrar_eje/', 'apps.ejes.views.RegistrarEje', name="registrar_eje",),
    url(r'^actualizar_eje/(?P<pk>\d+)/$', 'apps.ejes.views.ActualizarEje', name="actualizar_eje",),
    url(r'^eliminar_eje/(?P<pk>\d+)/$', 'apps.ejes.views.EliminarEje', name="eliminar_eje",),
    #url(r'^busqueda_ajax_centros/$','apps.registro.views.BuscarAjaxCentros', name='listar_centros',),
    #url(r'^busqueda_ajax2/$','apps.registro.views.BuscarAjaxPar', name='listar_municipios',),
    url(r'^data/', 'apps.ejes.views.load_data', name="datos_ejes",),  # URL de Importación para la data
]
