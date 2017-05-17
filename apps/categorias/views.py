# -*- encoding: utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bitacora
from .models import Categoria
from .forms import FormCategorias
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import os
import csv
from django.conf import settings


# Create your views here.
@login_required(login_url='/iniciar/login/')
def ListarCategorias(request):
    """
    Función para listar los cargos. Se usa 'context_object_name' para enviar los registros del
    modelo a la vista especificada.

    :param cargos: variable que contiene todos los objetos del modelo Categoria.
    :param paginator: variable que hace una lista del contenido de la variable cargos.
    :param page: variable que obtiene el número de página.
    """
    listar_categorias = Categoria.objects.all()
    #paginator = Paginator(cargos, 10)  # Show 5 contacts per page
    #page = request.GET.get('page')
    #try:
    #    listar_categorias = paginator.page(page)
    #except PageNotAnInteger:
    #    # If page is not an integer, deliver first page.
    #    listar_categorias = paginator.page(1)
    #except EmptyPage:
    #    # If page is out of range (e.g. 9999), deliver last page of results.
    #    listar_categorias = paginator.page(paginator.num_pages)
    ctx = {'listar_categorias': listar_categorias}  # ctx = Contexto
    return render_to_response('categorias/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def RegistrarCategoria(request):  # Forma actual
    """
        Función para registrar una nueva categoria.

        :param num_categorias: variable donde se cuenta el número de objetos del modelo Categoria.
    """
    num_categorias = Categoria.objects.count()  # Número de cargos registrados
    # Conversión del número de cargos anteponiendo ceros a la izquierda hasta alcanzar el límite de 4 dígitos
    num_categorias = "CT"+str(num_categorias+1).zfill(4)
    #estados = Estado.objects.all()
    if request.method == 'POST':
        #print "DATOS: ", request
        from_rcategoria = FormCategorias(request.POST, request.FILES)
        if from_rcategoria.is_valid():
            nuevo_rcategoria = from_rcategoria.save(commit=False)
            nuevo_rcategoria.user = request.user.username
            nuevo_rcategoria.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Registro de nueva categoria ("+str(request.POST['cod_categoria'])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/categorias/listar_categorias')
    else:
        from_rcategoria = FormCategorias()
    ctx = {'from_rcategoria': from_rcategoria, 'num_categorias': num_categorias}  # ctx = Contexto (datos de los modelos)
    return render_to_response('categorias/nueva_categoria.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ActualizarCategoria(request, pk):
    """
        Función para editar los datos de una categoria.

        :param obj_rcategoria: variable que obtiene el objeto (categoria) que coincida con el valor del parámetro pk
    """
    #estados = Estado.objects.all()
    obj_rcategoria = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        form_rcategoria = FormCategorias(request.POST, request.FILES, instance=obj_rcategoria)
        if form_rcategoria.is_valid():
            edit_rcategoria = form_rcategoria.save(commit=False)
            edit_rcategoria.user = request.user.username
            edit_rcategoria.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Actualización de la categoría '"+str(request.POST['cod_categoria'])+"'...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/categorias/listar_categorias')
    else:
        form_rcategoria = FormCategorias(instance=obj_rcategoria)
    ctx = {'form_rcategoria': form_rcategoria, 'obj_rcategoria': obj_rcategoria}  # ctx = Contexto
    return render_to_response('categorias/edit_categoria.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def EliminarCategoria(request, pk):
    """
        Función para eliminar una categoría. Se usa 'context_object_name' para enviar el registro del modelo
        a la vista especificada.

        :param obj_rcategoria: variable que obtiene el objeto (categoría) que coincida con el valor del parámetro pk
    """
    obj_rcategoria = Categoria.objects.get(id=pk)
    obj_rcategoria.delete()
    x = datetime.datetime.now()
    #print "Fecha y Hora: "+str(x)
    reg_bitacora = Bitacora(
        accion="Eliminación de la categoría '"+str(obj_rcategoria.cod_categoria)+"'...",
        usuario=request.user.username,
        fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/categorias/listar_categorias')


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

    reader = csv.reader(open(DIR_URL+str("/apps/categorias/script/categorias.csv")))
    # Recorrido de los registros
    for row in reader:
        data = row[0].split(';')
        consulta_categoria = Categoria.objects.filter(cod_categoria=data[0])
        if consulta_categoria:
            print "Ya existe..."
        else:
            categoria = Categoria(
                cod_categoria=data[0],
                categoria=data[1],
                user_create_id=data[2],
                )
            categoria.save()

            x = datetime.datetime.now()
            reg_bitacora = Bitacora(
                accion="Registro de nueva categoría desde csv ("+str(data[0])+")...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()

    return HttpResponseRedirect('/categorias/listar_categorias')
#======================================================================================
