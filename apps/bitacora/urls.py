# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ListarBitacora, FormReporteBitacora, ReporteBitacoraEsp, ReporteBitacoraGen

"""
    Nota: Para cada elemento 'url' de 'urlpatterns' se debe tener en cuenta que el segundo argumento se
    indica de acuerdo a lo declarado en el view, ya que si las vista son declaradas con clases la sintaxis
    es clase.as_view() y si las vistas son declaradas con funciones entonces la sintaxis cambia a
    'ruta.del.views.funcion'
"""

urlpatterns = [
    url(r'^listar_bitacora/$', 'apps.bitacora.views.ListarBitacora', name="listar_bitacora",),
    url(r'^form_reporte_bitacora/$', 'apps.bitacora.views.FormReporteBitacora', name="form_reporte_bitacora",),
    url(r'^reporte_bitacora_esp/(?P<usu>\w+)/(?P<f_desde>[0-9]{2}\-[0-9]{2}\-[0-9]{4})/(?P<f_hasta>[0-9]{2}\-[0-9]{2}\-[0-9]{4})/$', 'apps.bitacora.views.ReporteBitacoraEsp', name="reporte_bitacora_esp"),
    url(r'^reporte_bitacora_gen/(?P<usu>\w+)/$', 'apps.bitacora.views.ReporteBitacoraGen', name="reporte_bitacora_gen"),
    #url(r'^detallado/(?P<from_date>[0-9]{2}\-[0-9]{2}\-[0-9]{4})/(?P<to_date>[0-9]{2}\-[0-9]{2}\-[0-9]{4})$', ReporteDetallado.as_view()),
]
