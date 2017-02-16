# -*- encoding: utf-8 -*-
import datetime
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Bitacora
from .models import Municipio  # Modelo Municipio
from .forms import FormMunicipio  # Vista Forms Municipio
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
import csv  # Libreria para inportar CSV
import os
from apps.topologia.estados.models import Estado
from apps.circuitos.models import Circuitos


#=====================================================================================
#                            # Metodo RegistrarMunicipio
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def RegistrarMunicipio(request):
    """
        Función para registrar un municipio nuevo.
	
	:param lista_estado: variable que contiene todos los objetos del modelo Estado.
	:param lista_circuito: variable que contiene todos los objetos del modelo Circuitos.
	:param mun: variable que contiene todos los objetos del modelo Municipio.
	:param count_m: variable que contiene un número entero representativo de la cantidad de registros del modelo Municipio.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    lista_estado = Estado.objects.all()
    lista_circuito = Circuitos.objects.all()
    mun = Municipio.objects.all()
    count_m = len(mun) + 1
    if request.method == 'POST':
        form_reg_mun = FormMunicipio(request.POST, request.FILES)
        if form_reg_mun.is_valid():
            new_reg_mun = form_reg_mun.save(commit=False)
            new_reg_mun.user = request.user.username
            new_reg_mun.save()
            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Registro de nuevo municipio ("+str(request.POST['cod_municipio'])+")...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()
	    return HttpResponseRedirect('/municipio/listar_municipios')
    else:
        form_reg_mun = FormMunicipio()
    ctx = {'form_reg_mun': form_reg_mun, 'lista_estado': lista_estado, 'lista_circuito': lista_circuito, 'count_m': count_m}
    return render_to_response('topologia/municipio/registrar_municipio.html', ctx, context_instance=RequestContext(request))


#=====================================================================================
#                            # Clase RegistrarEstado
#=====================================================================================

@login_required(login_url='/iniciar/login/')
def ActualizarMunicipio(request, pk):
    """
        Función para actualizar un municipio.
	
	:param lista_estado: variable que contiene todos los objetos del modelo Estado.
	:param lista_circuito: variable que contiene todos los objetos del modelo Circuitos.
	:param obj_reg_mun: variable que contiene el objeto del modelo Municipio que coincide con el id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    lista_estado = Estado.objects.all()
    lista_circuito = Circuitos.objects.all()
    obj_reg_mun = Municipio.objects.get(id=pk)
    if request.method == 'POST':
        form_reg_mun = FormMunicipio(request.POST, request.FILES, instance=obj_reg_mun)
        if form_reg_mun.is_valid():
            edit_reg_mun = form_reg_mun.save(commit=False)
            edit_reg_mun.user = request.user.username
            edit_reg_mun.save()
	    x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Actualización del municipio '"+str(request.POST['cod_municipio'])+"'...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/municipio/listar_municipios')
    else:
        form_reg_mun = FormMunicipio(instance=obj_reg_mun)
    ctx = {'form_reg_mun': form_reg_mun, 'obj_reg_mun': obj_reg_mun, 'lista_estado': lista_estado, 'lista_circuito': lista_circuito}  # ctx = Contexto
    return render_to_response('topologia/municipio/actualizar_municipio.html', ctx, context_instance=RequestContext(request))


#=====================================================================================
#                            # Clase RegistrarEstado
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def EliminarMunicipio(request, pk):
    """
        Función para eliminar un municipio.
	
	:param obj_mun: variable que contiene el objeto del modelo Municipio que coincide con el id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    obj_mun = Municipio.objects.get(id=pk)
    obj_mun.delete()
    x = datetime.datetime.now()
    reg_bitacora = Bitacora(
    	accion="Eliminación del municipio '"+str(obj_mun.cod_municipio)+"'...",
	usuario=request.user.username,
	fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/municipio/listar_municipios')


#======================================================================================
              # Metodo para listar Registros y Paginacion
#======================================================================================
@login_required(login_url='/iniciar/login/')
def ListarMunicipio(request):
    """
        Función para listar los municipios.

        :param lista_municipio: variable que contiene todos los objetos del modelo Municipio.
    """
    lista_municipio = Municipio.objects.all()
    ctx = {'lista_municipio': lista_municipio, }  # ctx = Contexto
    return render_to_response('topologia/municipio/lista_municipio.html', ctx, context_instance=RequestContext(request))


#======================================================================================
# Url Importar data CSV
#======================================================================================
@login_required(login_url='/iniciar/login/')
def load_data(request):
    """
    Función para la carga de la data por defecto del módulo de municipios.

    :param DIR_URL: variable que almacena la ruta del proyecto.
    :param x: variable que contiene la fecha y hora actual.
    :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """

    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = os.getcwd()

    reader = csv.reader(open(DIR_URL+str("/apps/topologia/municipios/script/municipio.csv")))

    # Recorrido de los registros
    for row in reader:
        data = row[0].split(';')
        municipio = Municipio.objects.filter(estado_id=data[1],cod_municipio=data[2])
        if municipio:
        	print "Ya existe"
        	return HttpResponseRedirect('/municipio/listar_municipios')
        else:
			centro = Municipio(
				municipio=data[0],
				cod_municipio=data[2],
				estado_id=data[1],
				circuito_id=data[3],)
			centro.save()
			x = datetime.datetime.now()
		        reg_bitacora = Bitacora(
		    	    accion="Registro de nuevo municipio desde csv ("+str(data[0])+")...",
			    usuario=request.user.username,
			    fecha=x,)
		        reg_bitacora.save()

    return HttpResponseRedirect('/municipio/listar_municipios')
#======================================================================================
