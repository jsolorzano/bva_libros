# -*- encoding: utf-8 -*-
import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Bitacora
from .models import Estado
from .forms import FormEstado
from django.views.generic.dates import ArchiveIndexView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.contrib import messages # Metodo para la validacion de los campos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Paginacion
from django.contrib.auth.decorators import login_required # Forma para impedir el acceso al sistema
import os
import csv
#=====================================================================================
#                            # Clase RegistrarEstado
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def RegistrarEstado(request):
    """
        Función para registrar un estado nuevo.

        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    if request.method=='POST':
        form_regestado = FormEstado(request.POST, request.FILES)
        if form_regestado.is_valid():
            nuevo_regestado = form_regestado.save(commit=False)
            nuevo_regestado.user = request.user.username
            nuevo_regestado.save()
            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Registro de nuevo estado ("+str(request.POST['cod_estado'])+")...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()
	    return HttpResponseRedirect('/estado/lista_estado')
    else:
         form_regestado = FormEstado()
    ctx = {'form_regestado':form_regestado} # ctx = Contexto
    return render_to_response('topologia/estado/registrar_estado.html',ctx, context_instance=RequestContext(request))
    

#=====================================================================================
                            # Clase ActualizarEstado
#=====================================================================================
@login_required(login_url='/iniciar/login/')
def ActualizarEstado(request,pk):
    """
        Función para actualizar los datos de un estado.

        :param obj_regestado: variable que contiene el objeto del modelo Estado que coincide con un id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    obj_regestado = Estado.objects.get(id=pk)
    if request.method=='POST':
        form_regestado = FormEstado(request.POST, request.FILES, instance=obj_regestado)
        if form_regestado.is_valid():
            edit_regestado = form_regestado.save(commit=False)
            edit_regestado.user = request.user.username
            edit_regestado.save()
	    x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Actualización del estado '"+str(request.POST['cod_estado'])+"'...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/estado/lista_estado')
    else:
        form_regestado = FormEstado(instance=obj_regestado)
    ctx = {'form_regestado':form_regestado,'obj_regestado':obj_regestado} # ctx = Contexto
    return render_to_response('topologia/estado/actualizar_estado.html',ctx, context_instance=RequestContext(request))

#=====================================================================================
                            # Clase EliminarEstado
#=====================================================================================
def EliminarEstado(request,pk):
    """
        Función para eliminar un estado.

        :param obj_regestado: variable que contiene el objeto del modelo Estado que coincide con un id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    obj_regestado = Estado.objects.get(id=pk)
    obj_regestado.delete()
    x = datetime.datetime.now()
    reg_bitacora = Bitacora(
    	accion="Eliminación del estado '"+str(obj_regestado.cod_estado)+"'...",
	usuario=request.user.username,
	fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/estado/lista_estado')
#======================================================================================
# Metodo para listar Registros y Paginacion
#======================================================================================
@login_required(login_url='/iniciar/login/')
def ListarEstado(request):
    """
        Función para listar los estados.

        :param lista_estados: variable que contiene todos los objetos del modelo Estado.
    """
    lista_estados    = Estado.objects.all()
    ctx          = {'lista_estados':lista_estados,} # ctx = Contexto
    return render_to_response('topologia/estado/lista_estado.html',ctx, context_instance=RequestContext(request))

#======================================================================================
                    # Metodo para renderizar a /
#=====================================================================================

def base_view(request):
    
    return render_to_response('base/base.html',locals(), context_instance=RequestContext(request))
#======================================================================================
# Url Importar data CSV
#======================================================================================
@login_required(login_url='/iniciar/login/')
def load_data(request):
    """
    Función para la carga de la data por defecto del módulo de estados.

    :param DIR_URL: variable que almacena la ruta del proyecto.
    :param x: variable que contiene la fecha y hora actual.
    :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """

    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = os.getcwd()

    reader = csv.reader(open(DIR_URL+str("/apps/topologia/estados/script/estados.csv")))
    
    # Recorrido de los registros
    for row in reader:
        data = row[0].split(';')
        estado = Estado.objects.filter(cod_estado=data[0])
        if estado:
            print "Ya existe"
            return HttpResponseRedirect('/estado/lista_estado')
        else:
            centro = Estado(
                cod_estado = data[0],
                estado = data[1],
                )
            centro.save()
            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
            	accion="Registro de nuevo estado desde csv ("+str(data[0])+")...",
		usuario=request.user.username,
		fecha=x,)
            reg_bitacora.save()

    return HttpResponseRedirect('/estado/lista_estado')
#======================================================================================

def custom_404(request):
    return render_to_response('404.html', RequestContext(request))
