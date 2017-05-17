# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarLibros, RegistrarLibro, ActualizarLibro, EliminarLibro

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    #url(r'^', 'apps.libros.views.ListarLibros', name="listar_libros",),
    url(r'^listar_libros/$', 'apps.libros.views.ListarLibros', name="listar_libros",),
    url(r'^listar_libros_filtro/(?P<cod_sede>\w+)/(?P<cod_categoria>\w+)/(?P<cod_autor>\w+)/(?P<cod_editorial>\w+)/$', 'apps.libros.views.ListarLibrosFiltro', name="listar_libros_filtro",),
    url(r'^registrar_libro/', 'apps.libros.views.RegistrarLibro', name="registrar_libro",),
    url(r'^actualizar_libro/(?P<pk>\d+)/$', 'apps.libros.views.ActualizarLibro', name="actualizar_libro",),
    url(r'^eliminar_libro/(?P<pk>\d+)/$', 'apps.libros.views.EliminarLibro', name="eliminar_libro",),
    #url(r'^form_reporte_libro/$', 'apps.libro.views.FormReporteLibro', name="form_reporte_libro",),
    #url(r'^reporte_libro/(?P<libro>\d+)/$', 'apps.libro.views.ReporteLibro', name="reporte_libro"),
    #url(r'^busqueda_agremiado/$', 'apps.directiva.views.BuscarAgremiado', name='busqueda_agremiado',),
    #url(r'^nivel_cargo/$', 'apps.directiva.views.NivelCargo', name='nivel_cargo',),
    #url(r'^busqueda_directivo/$', 'apps.directiva.views.BuscarDirectivo', name='busqueda_directivo',),
    #url(r'^data/', 'apps.directiva.views.load_data', name="datos_electores",), # URL de Importación para la data
]
