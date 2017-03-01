# -*- encoding: utf-8 -*-
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from .models import Parroquia
from .models import Bitacora
from .forms import FormParroquia
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Paginacion
from django.contrib.auth.decorators import login_required # Forma para impedir el acceso al sistema
from django.core import serializers
import csv # Libreria para inportar CSV
import os
from django.db import connection
#=====================================================================================
#                            # Clase RegistrarParroquia
#=====================================================================================

@login_required(login_url='/iniciar/login/')
def RegistrarParroquia(request):
    """
        Función para registrar una parroquia nueva.
	
	:param list_e: variable que contiene todos los objetos del modelo Estado.
	:param list_m: variable que contiene todos los objetos del modelo Municipio.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    list_e = Estado.objects.all()
    list_m = Municipio.objects.all()
    if request.method=='POST':
        form_reg_par = FormParroquia(request.POST, request.FILES)
        if form_reg_par.is_valid():
            new_reg_par = form_reg_par.save(commit=False)
            new_reg_par.user = request.user.username
            new_reg_par.save()
	    x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Registro de nueva parroquia ("+str(request.POST['cod_parroquia'])+")...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()
	    return HttpResponseRedirect('/parroquia/listar_parroquia')
    else:
         form_reg_par = FormParroquia()
    ctx = {'form_reg_par':form_reg_par,'list_e':list_e,'list_m':list_m} # ctx = Contexto
    return render_to_response('topologia/parroquia/registrar_parroquias.html',ctx, context_instance=RequestContext(request))

#=====================================================================================
                            # Metodo ActualizarParroquia
#=====================================================================================

@login_required(login_url='/iniciar/login/')
def ActualizarParroquia(request,pk):
    """
        Función para actualizar una parroquia.
	
	:param list_e: variable que contiene todos los objetos del modelo Estado.
	:param lista_m: variable que contiene todos los objetos del modelo Municipio.
	:param obj_reg_parr: variable que contiene el objeto del modelo Parroquia que coincide con el id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    list_e = Estado.objects.all()
    list_m = Municipio.objects.all()
    obj_reg_parr = Parroquia.objects.get(id=pk)
    if request.method=='POST':
        form_reg_parr = FormParroquia(request.POST, request.FILES, instance=obj_reg_parr)
        if form_reg_parr.is_valid():
            edit_reg_parr = form_reg_parr.save(commit=False)
            edit_reg_parr.user = request.user.username
            edit_reg_parr.save()
	    x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Actualización de la parroquia '"+str(request.POST['cod_parroquia'])+"'...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/parroquia/listar_parroquia')
    else:
        form_reg_parr = FormParroquia(instance=obj_reg_parr)
    ctx = {'form_reg_parr':form_reg_parr,'obj_reg_parr':obj_reg_parr,'list_e':list_e,'list_m':list_m} # ctx = Contexto
    return render_to_response('topologia/parroquia/actualizar_parroquias.html',ctx, context_instance=RequestContext(request))

#=====================================================================================
                            # Metodo EliminarParroquia
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def EliminarParroquia(request,pk):
    """
        Función para eliminar una parroquia.
	
	:param obj_reg_pa: variable que contiene el objeto del modelo Parroquia que coincide con el id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    obj_reg_pa = Parroquia.objects.get(id=pk)
    obj_reg_pa.delete()
    x = datetime.datetime.now()
    reg_bitacora = Bitacora(
    	accion="Eliminación de la parroquia '"+str(obj_reg_pa.cod_parroquia)+"'...",
	usuario=request.user.username,
	fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/parroquia/listar_parroquia')

#=====================================================================================
                            # Metodo BuscarAjaxParr json
#=====================================================================================
def BuscarAjaxMun(request):
    """
        Función para buscar los datos de una parroquia específica.
	
	:param id_est: variable que captura el id de un estado vía url.
        :param municipios: variable que contiene el objeto del modelo Municipio que coincide con el id dado.
        :param data: variable que serializa en formato json los datos contenidos en la variable municipios.
    """
    id_est = request.GET['id']
    municipios = Municipio.objects.filter(estado_id=id_est)
    data = serializers.serialize('json',municipios,
                                       fields=('cod_municipio','municipio'))
    #print "LISTA DE MUNICIPIOS: ",data
    
    return HttpResponse(data, content_type='application/json')


@login_required(login_url='/iniciar/login/')
def BuscarAjaxPar(request):
    """
        Función para buscar los datos de una parroquia específica.
	
	:param id_est: variable que captura el id de un estado vía url.
	:param id_mun: variable que captura el id de un municipio vía url.
        :param parroquias: variable que contiene el objeto del modelo Parroquia que coincide con el id dado.
        :param data: variable que serializa en formato json los datos contenidos en la variable parroquias.
    """
    id_est = request.GET['id_est']
    id_mun = request.GET['id_mun']
    parroquias = Parroquia.objects.filter(estado_id=id_est,municipio=id_mun)
    data = serializers.serialize('json',parroquias,
                                       fields=('cod_parroquia','parroquia'))
    return HttpResponse(data, content_type='application/json')

#======================================================================================
#                  Metodo para listar Registros y Paginacion
#======================================================================================
@login_required(login_url='/iniciar/login/')
def ListarParroquia(request):
    """
        Función para listar los municipios.

        :param lista_estado: variable que contiene todos los objetos del modelo Estado.
	:param lista_municipio: variable que contiene todos los objetos del modelo Municipio.
	:param lista_parroquia: variable que contiene todos los objetos del modelo Parroquia.
	:param array: variable que contiene un diccionario con los todos registros de los modelos de Estado, Municipio y Parroquia.
    """
    list_parroquia = Parroquia.objects.all().order_by('municipio','parroquia')
    list_estado = Estado.objects.all()
    list_municipio = Municipio.objects.all()
    
    array = {
        'list_parroquia' : list_parroquia,
        'list_estado'    : list_estado,
        'list_municipio' : list_municipio,
    }
    return render_to_response('topologia/parroquia/lista_parroquia.html', array, context_instance = RequestContext(request))

#=====================================================================================
#                        # Metetodo load_data_parroquia
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def load_data_parroquia(request):
    """
    Función para la carga de la data por defecto del módulo de parroquias.

    :param DIR_URL: variable que almacena la ruta del proyecto.
    :param x: variable que contiene la fecha y hora actual.
    :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    
    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = os.getcwd()
    
    reader = csv.reader(open(DIR_URL+str("/apps/topologia/parroquias/script/parroquias.csv")))
    
    for row in reader:
        data = row[0].split(';')
        parr = Parroquia.objects.filter(estado_id=data[1],municipio=data[2],cod_parroquia=data[3])
        if parr:
            print "Ya existe"
            return HttpResponseRedirect('/parroquia/listar_parroquia')
        else:
            parroquia = Parroquia(
                #id             = data[0],
                parroquia       = data[0],
                estado_id       = data[1],
                municipio       = data[2],
                cod_parroquia   = data[3],
                )
            parroquia.save()
	    x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Registro de nueva parroquia desde csv ("+str(data[0])+")...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()
    return HttpResponseRedirect('/parroquia/listar_parroquia')
#=====================================================================================
