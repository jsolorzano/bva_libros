# -*- encoding: utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bitacora
from .models import Eje
from .forms import FormEjes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import os
import csv
from django.conf import settings


# Create your views here.
@login_required(login_url='/iniciar/login/')
def ListarEjes(request):
    """
    Función para listar los cargos. Se usa 'context_object_name' para enviar los registros del
    modelo a la vista especificada.

    :param listar_ejes: variable que contiene todos los objetos del modelo Eje.
    :param paginator: variable que hace una lista del contenido de la variable cargos.
    :param page: variable que obtiene el número de página.
    """
    listar_ejes = Eje.objects.all()
    #paginator = Paginator(cargos, 10)  # Show 5 contacts per page
    #page = request.GET.get('page')
    #try:
    #    listar_ejes = paginator.page(page)
    #except PageNotAnInteger:
    #    # If page is not an integer, deliver first page.
    #    listar_ejes = paginator.page(1)
    #except EmptyPage:
    #    # If page is out of range (e.g. 9999), deliver last page of results.
    #    listar_ejes = paginator.page(paginator.num_pages)
    ctx = {'listar_ejes': listar_ejes}  # ctx = Contexto
    return render_to_response('ejes/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def RegistrarEje(request):  # Forma actual
    """
        Función para registrar un nuevo eje.

        :param num_ejes: variable donde se cuenta el número de objetos del modelo Eje.
    """
    num_ejes = Eje.objects.count()  # Número de cargos registrados
    # Conversión del número de cargos anteponiendo ceros a la izquierda hasta alcanzar el límite de 4 dígitos
    num_ejes = "E"+str(num_ejes+1).zfill(4)
    #estados = Estado.objects.all()
    if request.method == 'POST':
        #print "DATOS: ", request
        from_reje = FormEjes(request.POST, request.FILES)
        if from_reje.is_valid():
            nuevo_reje = from_reje.save(commit=False)
            nuevo_reje.user = request.user.username
            nuevo_reje.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Registro de nuevo eje ("+str(request.POST['cod_eje'])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/ejes/listar_ejes')
    else:
        from_reje = FormEjes()
    ctx = {'from_reje': from_reje, 'num_ejes': num_ejes}  # ctx = Contexto (datos de los modelos)
    return render_to_response('ejes/nuevo_eje.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ActualizarEje(request, pk):
    """
        Función para editar los datos de un eje.

        :param obj_reje: variable que obtiene el objeto (eje) que coincida con el valor del parámetro pk
    """
    #estados = Estado.objects.all()
    obj_reje = Eje.objects.get(id=pk)
    if request.method == 'POST':
        form_reje = FormEjes(request.POST, request.FILES, instance=obj_reje)
        if form_reje.is_valid():
            edit_reje = form_reje.save(commit=False)
            edit_reje.user = request.user.username
            edit_reje.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Actualización del eje '"+str(request.POST['cod_eje'])+"'...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/ejes/listar_ejes')
    else:
        form_reje = FormEjes(instance=obj_reje)
    ctx = {'form_reje': form_reje, 'obj_reje': obj_reje}  # ctx = Contexto
    return render_to_response('ejes/edit_eje.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def EliminarEje(request, pk):
    """
        Función para eliminar un eje. Se usa 'context_object_name' para enviar el registro del modelo
        a la vista especificada.

        :param obj_reje: variable que obtiene el objeto (eje) que coincida con el valor del parámetro pk
    """
    obj_reje = Eje.objects.get(id=pk)
    obj_reje.delete()
    x = datetime.datetime.now()
    #print "Fecha y Hora: "+str(x)
    reg_bitacora = Bitacora(
        accion="Eliminación del eje '"+str(obj_reje.cod_eje)+"'...",
        usuario=request.user.username,
        fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/ejes/listar_ejes')


#======================================================================================
# Importar data CSV de los cargos predefinidos
#======================================================================================
@login_required(login_url='/iniciar/login/')
def load_data(request):
    """
    Función para la carga de la data por defecto del módulo de ejes.

    :param DIR_URL: variable que almacena la ruta del proyecto.
    """

    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = settings.BASE_DIR
#    print "Ruta: ", settings.BASE_DIR
    reader = csv.reader(open(DIR_URL+str("/apps/ejes/script/ejes.csv")))
    # Recorrido de los registros
    for row in reader:
        data = row[0].split(';')
        consulta_eje = Eje.objects.filter(cod_eje=data[0])
        if consulta_eje:
            print "Ya existe..."
        else:
            eje = Eje(
                cod_eje=data[0],
                eje=data[1],
                user_create_id=data[2],
                )
            eje.save()
            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
                accion="Registro de nuevo eje desde csv ("+str(data[0])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()

    return HttpResponseRedirect('/ejes/listar_ejes')
#======================================================================================
