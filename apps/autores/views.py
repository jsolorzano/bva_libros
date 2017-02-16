# -*- encoding: utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bitacora
from .models import Autor
from .forms import FormAutores
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginación
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import os
import csv
from django.conf import settings


# Create your views here. (Crea tus vistas aquí)
@login_required(login_url='/iniciar/login/')
def ListarAutores(request):
    """
    Función para listar los autores.

    :param listar_autores: variable que contiene todos los objetos del modelo Autor.
    """
    listar_autores = Autor.objects.all()
    ctx = {'listar_autores': listar_autores}  # ctx = Contexto
    return render_to_response('autores/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def RegistrarAutor(request):  # Forma actual
    """
        Función para registrar uno nuevo autor.

        :param num_autores: variable donde se cuenta el número de objetos del modelo Autor.
    """
    num_autores = Autor.objects.count()  # Número de cargos registrados
    # Conversión del número de cargos anteponiendo ceros a la izquierda hasta alcanzar el límite de 4 dígitos
    num_autores = "A"+str(num_autores+1).zfill(4)
    if request.method == 'POST':
        #print "DATOS: ", request
        from_rautor = FormAutores(request.POST, request.FILES)
        if from_rautor.is_valid():
            nuevo_rautor = from_rautor.save(commit=False)
            nuevo_rautor.user = request.user.username
            nuevo_rautor.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Registro de nuevo autor ("+str(request.POST['cod_autor'])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/autores/listar_autores')
    else:
        from_rautor = FormAutores()
    ctx = {'from_rautor': from_rautor, 'num_autores': num_autores}  # ctx = Contexto (datos de los modelos)
    return render_to_response('autores/nuevo_autor.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ActualizarAutor(request, pk):
    """
        Función para editar los datos de un autor.

        :param obj_rautor: variable que obtiene el objeto (autor) que coincida con el valor del parámetro pk
    """
    #estados = Estado.objects.all()
    obj_rautor = Autor.objects.get(id=pk)
    if request.method == 'POST':
        form_rautor = FormAutores(request.POST, request.FILES, instance=obj_rautor)
        if form_rautor.is_valid():
            edit_rautor = form_rautor.save(commit=False)
            edit_rautor.user = request.user.username
            edit_rautor.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Actualización del autor '"+str(request.POST['cod_autor'])+"'...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/autores/listar_autores')
    else:
        form_rautor = FormAutores(instance=obj_rautor)
    ctx = {'form_rAutor': form_rautor, 'obj_rautor': obj_rautor}  # ctx = Contexto
    return render_to_response('autores/edit_autor.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def EliminarAutor(request, pk):
    """
        Función para eliminar una categoría. Se usa 'context_object_name' para enviar el registro del modelo
        a la vista especificada.

        :param obj_rautor: variable que obtiene el objeto (categoría) que coincida con el valor del parámetro pk
    """
    obj_rautor = Autor.objects.get(id=pk)
    obj_rautor.delete()
    x = datetime.datetime.now()
    #print "Fecha y Hora: "+str(x)
    reg_bitacora = Bitacora(
        accion="Eliminación del autor '"+str(obj_rautor.cod_autor)+"'...",
        usuario=request.user.username,
        fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/autores/listar_autores')


#======================================================================================
# Importar data CSV de los cargos predefinidos
#======================================================================================
@login_required(login_url='/iniciar/login/')
def load_data(request):
    """
    Función para la carga de la data por defecto del módulo de autores.

    :param DIR_URL: variable que almacena la ruta del proyecto.
    """

    os.path.dirname(os.path.abspath(__file__))

    DIR_URL = settings.BASE_DIR

    reader = csv.reader(open(DIR_URL+str("/apps/autores/script/autores.csv")))
    # Recorrido de los registros
    for row in reader:
        data = row[0].split(';')
        consulta_autor = Autor.objects.filter(cod_autor=data[0])
        if consulta_autor:
            print "Ya existe..."
        else:
            autor = Autor(
                cod_autor=data[0],
                autor=data[1],
                user_create_id=data[2],
                )
            autor.save()

            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
                accion="Registro de nuevo autor desde csv ("+str(data[0])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()

    return HttpResponseRedirect('/autores/listar_autores')
#======================================================================================
