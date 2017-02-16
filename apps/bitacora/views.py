# -*- encoding: utf-8 -*-
import datetime
import time
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bitacora
from .forms import FormBitacora
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import os
import csv
#import report_bitacora
#import report_bitacora_gen
from apps.bitacora.reportes import report_bitacora
from apps.bitacora.reportes import report_bitacora_gen
from django.contrib.auth.models import User  # Importación del modelo de usuarios
from django.db import connection, transaction  # Modelos para consulta directa a la base de datos.


# Create your views here.
@login_required(login_url='/iniciar/login/')
def ListarBitacora(request):
    """
    Función para listar la bitacora. Se usa 'context_object_name' para enviar los registros del
    modelo a la vista especificada.


    :listar_bitacora: variable que contiene todos los objetos del modelo Bitacora.
    :param paginator: variable que hace una lista del contenido de la variable cargos.
    :param page: variable que obtiene el número de página.
    """
    listar_bitacora = Bitacora.objects.all()
    #paginator = Paginator(bitacora, 10)  # Muestra diez acciones por página
    #page = request.GET.get('page')
    #try:
    #    listar_bitacora = paginator.page(page)
    #except PageNotAnInteger:
    #    # If page is not an integer, deliver first page.
    #    listar_bitacora = paginator.page(1)
    #except EmptyPage:
    #    # If page is out of range (e.g. 9999), deliver last page of results.
    #    listar_bitacora = paginator.page(paginator.num_pages)
    ctx = {'listar_bitacora': listar_bitacora}  # ctx = Contexto
    return render_to_response('bitacora/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def FormReporteBitacora(request):
    """
    Función para generar una vista que permite filtrar las acciones según un usuario.
    """
    usuarios = User.objects.all()
    ctx = {'usuarios': usuarios}
    return render_to_response('bitacora/reporte_bitacora.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ReporteBitacoraEsp(request, usu, f_desde, f_hasta):
    """
    Función para generar un reporte en pdf de la bitacora de un usuario tomando un rango de fecha específico.
    """

    USU = usu

    #print USU
    #print f_desde
    #print f_hasta

    #consulta_bitacora = Bitacora.objects.filter(usuario=USU)

    try:
        cursor = connection.cursor()
        # Esta consulta trae los registros coincidentes con el rango de fechas dado y devuelve la fecha formateada en la zona horaria local.
        cursor.execute("SELECT accion, usuario, TO_CHAR(fecha::timestamp at time zone 'VET UTC-3:30 hours','dd/mm/yyyy HH24:MI:SS') FROM bitacora_bitacora WHERE fecha BETWEEN '"+str(f_desde)+"' AND '"+str(f_hasta)+"' AND usuario='"+str(USU)+"' ORDER BY fecha ASC")

        c = cursor.fetchall()
        #print "DATA: ", c
        data = c
    except:
        data = 0
    #
    #print consulta_bitacora.count()
    #
    if len(data) == 0:
        print "Está vacío..."
        response = "Disculpe, no hay registros con el rango de fecha especificado..."
        #data = serializers.serialize('json', consulta_bitacora, fields=('accion'))
        return HttpResponse(response, content_type='application/json')

    else:
        print "Tiene datos..."

        archivo, nombre_archivo = report_bitacora.gen_res_bitacora(data, USU, f_desde, f_hasta)
        response = HttpResponse(archivo.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="'+str(nombre_archivo)+'.pdf"'
        return response


@login_required(login_url='/iniciar/login/')
def ReporteBitacoraGen(request, usu):
    """
    Función para generar un reporte general en pdf de la bitacora de un usuario.
    """

    USU = usu

    #print USU

    fecha = time.strftime("%d/%m/%Y")

    hora = time.strftime("%I:%M %p")

    fecha = str(fecha)+" "+str(hora)

    #consulta_bitacora = Bitacora.objects.filter(usuario=USU)

    #print consulta_bitacora.count()

    try:
        cursor = connection.cursor()
        #id_count = 1
        cursor.execute("SELECT accion, usuario, TO_CHAR(fecha::timestamp at time zone 'VET UTC-3:30 hours','dd/mm/yyyy HH24:MI:SS') FROM bitacora_bitacora WHERE usuario='"+str(USU)+"' ORDER BY fecha ASC")

        c = cursor.fetchall()
        #print "DATA: ", c
        data = c
    except:
        data = 0

    if len(data) == 0:
        print "Está vacío..."
        response = "Disculpe, no hay registros para el usuario especificado..."
        #data = serializers.serialize('json', consulta_bitacora, fields=('accion'))
        return HttpResponse(response, content_type='application/json')

    else:
        print "Tiene datos..."

        archivo, nombre_archivo = report_bitacora_gen.gen_res_bitacora(data, USU, fecha)

        response = HttpResponse(archivo.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="'+str(nombre_archivo)+'.pdf"'
        return response
