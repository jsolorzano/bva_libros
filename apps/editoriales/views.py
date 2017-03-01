# -*- encoding: utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bitacora
from .models import Editorial
from .forms import FormEditoriales
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import os
import csv
from django.conf import settings


# Create your views here.
@login_required(login_url='/iniciar/login/')
def ListarEditoriales(request):
    """
    Función para listar los cargos. Se usa 'context_object_name' para enviar los registros del
    modelo a la vista especificada.

    :param cargos: variable que contiene todos los objetos del modelo editorial.
    :param paginator: variable que hace una lista del contenido de la variable cargos.
    :param page: variable que obtiene el número de página.
    """
    listar_editoriales = Editorial.objects.all()
    ctx = {'listar_editoriales': listar_editoriales}  # ctx = Contexto
    return render_to_response('editoriales/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def RegistrarEditorial(request):  # Forma actual
    """
        Función para registrar una nueva editorial.

        :param num_editoriales: variable donde se cuenta el número de objetos del modelo Editorial.
    """
    num_editoriales = Editorial.objects.count()  # Número de cargos registrados
    # Conversión del número de cargos anteponiendo ceros a la izquierda hasta alcanzar el límite de 4 dígitos
    num_editoriales = "ED"+str(num_editoriales+1).zfill(4)
    #estados = Estado.objects.all()
    if request.method == 'POST':
        #print "DATOS: ", request
        from_reditorial = FormEditoriales(request.POST, request.FILES)
        if from_reditorial.is_valid():
            nuevo_reditorial = from_reditorial.save(commit=False)
            nuevo_reditorial.user = request.user.username
            nuevo_reditorial.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Registro de nueva editorial ("+str(request.POST['cod_editorial'])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/editoriales/listar_editoriales')
    else:
        from_reditorial = FormEditoriales()
    ctx = {'from_reditorial': from_reditorial, 'num_editoriales': num_editoriales}  # ctx = Contexto (datos de los modelos)
    return render_to_response('editoriales/nueva_editorial.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ActualizarEditorial(request, pk):
    """
        Función para editar los datos de una editorial.

        :param obj_reditorial: variable que obtiene el objeto (editorial) que coincida con el valor del parámetro pk
    """
    #estados = Estado.objects.all()
    obj_reditorial = Editorial.objects.get(id=pk)
    if request.method == 'POST':
        form_reditorial = FormEditoriales(request.POST, request.FILES, instance=obj_reditorial)
        if form_reditorial.is_valid():
            edit_reditorial = form_reditorial.save(commit=False)
            edit_reditorial.user = request.user.username
            edit_reditorial.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Actualización de la categoría '"+str(request.POST['cod_editorial'])+"'...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/editoriales/listar_editoriales')
    else:
        form_reditorial = FormEditoriales(instance=obj_reditorial)
    ctx = {'form_reditorial': form_reditorial, 'obj_reditorial': obj_reditorial}  # ctx = Contexto
    return render_to_response('editoriales/edit_editorial.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def EliminarEditorial(request, pk):
    """
        Función para eliminar una categoría. Se usa 'context_object_name' para enviar el registro del modelo
        a la vista especificada.

        :param obj_reditorial: variable que obtiene el objeto (categoría) que coincida con el valor del parámetro pk
    """
    obj_reditorial = Editorial.objects.get(id=pk)
    obj_reditorial.delete()
    x = datetime.datetime.now()
    #print "Fecha y Hora: "+str(x)
    reg_bitacora = Bitacora(
        accion="Eliminación de la editorial '"+str(obj_reditorial.cod_editorial)+"'...",
        usuario=request.user.username,
        fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/editoriales/listar_editoriales')


#======================================================================================
# Importar data CSV de los cargos predefinidos
#======================================================================================
@login_required(login_url='/iniciar/login/')
def load_data(request):
    """
    Función para la carga de la data por defecto del módulo de categorías.

    :param DIR_URL: variable que almacena la ruta del proyecto.
    """

    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = settings.BASE_DIR

    reader = csv.reader(open(DIR_URL+str("/apps/editoriales/script/editoriales.csv")))
    # Recorrido de los registros
    for row in reader:
        data = row[0].split(';')
        consulta_editorial = Editorial.objects.filter(cod_editorial=data[0])
        if consulta_editorial:
            print "Ya existe..."
        else:
            editorial = Editorial(
                cod_editorial=data[0],
                editorial=data[1],
                user_create_id=data[2],
                )
            editorial.save()

            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
                accion="Registro de nueva editorial desde csv ("+str(data[0])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()

    return HttpResponseRedirect('/editoriales/listar_editoriales')
#======================================================================================
