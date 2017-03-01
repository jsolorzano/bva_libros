# -*- encoding: utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bitacora
from .models import Eje
from .models import Sede
from .forms import FormSedes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import os
import csv
from django.conf import settings


# Create your views here.
@login_required(login_url='/iniciar/login/')
def ListarSedes(request):
    """
        Función para listar las áreas de un cargo. Se usa 'context_object_name' para enviar los registros del
        modelo a la vista especificada.

        :param ejes: variable que contiene todos los objetos del modelo Eje.
        :param listar_sedes: variable que contiene todos los objetos del modelo Area.
    """
    ejes = Eje.objects.all()
    listar_sedes = Sede.objects.all()
    #paginator = Paginator(areas, 10)  # Show 5 contacts per page
    #page = request.GET.get('page')
    #try:
    #    listar_sedes = paginator.page(page)
    #except PageNotAnInteger:
    #    # If page is not an integer, deliver first page.
    #    listar_sedes = paginator.page(1)
    #except EmptyPage:
    #    # If page is out of range (e.g. 9999), deliver last page of results.
    #    listar_sedes = paginator.page(paginator.num_pages)
    ctx = {'listar_sedes': listar_sedes, 'ejes': ejes}  # ctx = Contexto
    return render_to_response('sedes/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def RegistrarSede(request):  # Forma actual
    """
        Función para registrar un área nueva.

        :param num_sedes: variable donde se cuenta el número de objetos del modelo Sede.
        :param ejes: variable que contiene todos los objetos del modelo Eje.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    num_sedes = Sede.objects.count()  # Número de áreas registradas
    # Conversión del números de áreas anteponiendo ceros a la izquierda hasta alcanzar el límite de 4 dígitos
    num_sedes = "S"+str(num_sedes+1).zfill(4)
    ejes = Eje.objects.all()
    if request.method == 'POST':
        #print "DATOS: ", request
        from_rsede = FormSedes(request.POST, request.FILES)
        if from_rsede.is_valid():
            nuevo_rsede = from_rsede.save(commit=False)
            nuevo_rsede.user = request.user.username
            nuevo_rsede.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Registro de nueva sede ("+str(request.POST['cod_sede'])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/sedes/listar_sedes')
    else:
        from_rsede = FormSedes()
    ctx = {'from_rsede': from_rsede, 'ejes': ejes, 'num_sedes': num_sedes}  # ctx = Contexto (datos de los modelos)
    return render_to_response('sedes/nueva_sede.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ActualizarSede(request, pk):
    """
        Función para editar los datos de un área.

        :param num_sedes: variable donde se cuenta el número de objetos del modelo Sede.
        :param ejes: variable que contiene todos los objetos del modelo Eje.
        :param obj_rsede: variable que contiene el objeto del modelo Sede que coincide con un id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    ejes = Eje.objects.all()
    obj_rsede = Sede.objects.get(id=pk)
    if request.method == 'POST':
        form_rsede = FormSedes(request.POST, request.FILES, instance=obj_rsede)
        if form_rsede.is_valid():
            edit_rsede = form_rsede.save(commit=False)
            edit_rsede.user = request.user.username
            edit_rsede.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Actualización del sede '"+str(request.POST['cod_sede'])+"'...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/sedes/listar_sedes')
    else:
        form_rsede = FormSedes(instance=obj_rsede)
    ctx = {'form_rsede': form_rsede, 'obj_rsede': obj_rsede, 'ejes': ejes}  # ctx = Contexto
    return render_to_response('sedes/editar_sede.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def EliminarSede(request, pk):
    """
        Función para eliminar una sede. Se usa 'context_object_name' para enviar el registro del modelo
        a la vista especificada.

        :param obj_rsede: variable que contiene el objeto del modelo Sede que coincide con un id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    obj_rsede = Sede.objects.get(id=pk)
    obj_rsede.delete()
    x = datetime.datetime.now()
    #print "Fecha y Hora: "+str(x)
    reg_bitacora = Bitacora(
        accion="Eliminación de la sede '"+str(obj_rsede.cod_sede)+"'...",
        usuario=request.user.username,
        fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/sedes/listar_sedes')


#======================================================================================
# Importar data CSV de los circuitos del estado Aragua
#======================================================================================
@login_required(login_url='/iniciar/login/')
def load_data(request):
    """
    Función para la carga de la data por defecto del módulo de sedes.

    :param DIR_URL: variable que almacena la ruta del proyecto.
    :param x: variable que contiene la fecha y hora actual.
    :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """

    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = settings.BASE_DIR

    reader = csv.reader(open(DIR_URL+str("/apps/sedes/script/sedes.csv")))
    # Recorrido de los registros
    for row in reader:
        data = row[0].split(';')
        consulta_sede = Sede.objects.filter(cod_sede=data[0])
        if consulta_sede:
            print "Ya existe..."
        else:
            sede = Sede(
                cod_sede=data[0],
                sede=data[2],
                descripcion=data[3],
                eje_id=data[1],
                user_create_id=data[4],)
            sede.save()

            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
                accion="Registro de nueva sede desde csv ("+str(data[0])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
    
    return HttpResponseRedirect('/sedes/listar_sedes')
#======================================================================================
