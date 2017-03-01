# -*- encoding: utf-8 -*-
import datetime
import time
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bitacora
#from apps.topologia.estados.models import Estado
#from apps.topologia.municipios.models import Municipio
#from apps.topologia.parroquias.models import Parroquia
#from apps.registro.models import FichaPersonal
from .models import Categoria
from apps.autores.models import Autor
from apps.editoriales.models import Editorial
from .models import Sede
from .models import Libros
from .forms import FormLibros
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.contrib.auth.decorators import login_required  # Forma para impedir el acceso al sistema
from django.core import serializers
import unicodedata
import os
import csv
from django.db import connection
from django.db.models import Q
#import report_libro
#from apps.libro.reportes import report_libro


def home(request):
    return HttpResponseRedirect('/libros/listar_libros')

# Create your views here.
#@login_required(login_url='/iniciar/login/')
def ListarLibros(request):
    """
        Función para listar las líneas del estado. Se usa 'context_object_name' para enviar los registros del
        modelo a la vista especificada.

        :param estados: variable que contiene todos los objetos del modelo Estado.
        :param municipios: variable que contiene todos los objetos del modelo Municipio.
        :param parroquias: variable que contiene todos los objetos del modelo Parroquia.
        :param listar_libros: variable que contiene todos los objetos del modelo Libro.
    """
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    editoriales = Editorial.objects.all()
    sedes = Sede.objects.all()
    #parroquias = Parroquia.objects.all()
    listar_libros = Libros.objects.all()
    ctx = {'listar_libros': listar_libros, 'categorias': categorias, 'sedes': sedes, 'autores': autores, 'editoriales': editoriales}  # ctx = Contexto
    return render_to_response('libros/lista.html', ctx, context_instance=RequestContext(request))
    

#@login_required(login_url='/iniciar/login/')
def ListarLibrosFiltro(request, cod_sede, cod_categoria, cod_autor, cod_editorial):
    """
        Función para listar las líneas del estado. Se usa 'context_object_name' para enviar los registros del
        modelo a la vista especificada.

        :param estados: variable que contiene todos los objetos del modelo Estado.
        :param municipios: variable que contiene todos los objetos del modelo Municipio.
        :param parroquias: variable que contiene todos los objetos del modelo Parroquia.
        :param listar_libros: variable que contiene todos los objetos del modelo Libro.
    """
    print "Codigo de la sede: ", cod_sede
    print "Codigo de la categoria: ", cod_categoria
    print "Codigo del autor: ", cod_autor
    print "Codigo de la editorial: ", cod_editorial
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    editoriales = Editorial.objects.all()
    sedes = Sede.objects.all()
    
    # Preparamos un dicconario con los argumentos seleccionados desde el template
    parametros = {'sede_id':cod_sede, 'categoria_id':cod_categoria, 'autor_id':cod_autor, 'editorial_id':cod_editorial}
    
    condicion = ""
    
    contador = 0
    
    # Construimos la condicón de la consulta con los argumentos seleccionados desde el template
    for p in parametros:
		if parametros[p] != '0':
			contador += 1
			if contador > 1:
				condicion += " AND "+p+"='"+parametros[p]+"'"
			else:
				condicion = "WHERE "+p+"='"+parametros[p]+"'"
    
    print condicion
    
    #~ listar_libros = Libros.objects.filter(Q(sede_id=cod_sede)| Q(categoria_id=cod_categoria)| Q(autor_id=cod_autor)| Q(editorial_id=cod_editorial))  # No es de utilidad en este caso
    listar_libros = Libros.objects.raw("SELECT * FROM libros_libros "+condicion)
    #~ 
    print listar_libros
    
    ctx = {'listar_libros': listar_libros, 'categorias': categorias, 'sedes': sedes, 'autores': autores, 'editoriales': editoriales}  # ctx = Contexto
    return render_to_response('libros/lista.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def RegistrarLibro(request):  # Forma actual
    """
        Función para registrar una libro de un estado.

        :param estados: variable que contiene todos los objetos del modelo Estado.
        :param municipios: variable que contiene todos los objetos del modelo Municipio.
        :param parroquias: variable que contiene todos los objetos del modelo Parroquia.
        :param num_libros: variable que contiene el código generado para la nueva línea.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    num_libros = Libros.objects.count()  # Número de circuitos registrados
    # Conversión del números de circuitos anteponiendo ceros a la izquierda hasta alcanzar el límite de 4 dígitos
    num_libros = "L"+str(num_libros+1).zfill(4)
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    editoriales = Editorial.objects.all()
    sedes = Sede.objects.all()
    #municipios = Municipio.objects.all()
    #parroquias = Parroquia.objects.all()
    if request.method == 'POST':
        #print "DATOS: ", request
        from_rlibro = FormLibros(request.POST, request.FILES)
        if from_rlibro.is_valid():
            nuevo_rlibro = from_rlibro.save(commit=False)
            nuevo_rlibro.user = request.user.username
            nuevo_rlibro.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            #acc = "Registro de nueva línea: "+request.POST['libro']+"..."
            acc = "Registro de nuevo libro ("+str(request.POST['cod_libro'])+")..."
            #print acc
            reg_bitacora = Bitacora(
                accion=acc,
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/libros/listar_libros')
    else:
        from_rlibro = FormLibros()
    ctx = {'from_rlibro': from_rlibro, 'cod_libro': num_libros, 'categorias': categorias, 'sedes': sedes, 'autores': autores, 'editoriales': editoriales}  # ctx = Contexto (datos de los modelos)
    return render_to_response('libros/nuevo_libro.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def ActualizarLibro(request, pk):
    """
        Función para editar los datos de una línea

        :param estados: variable que contiene todos los objetos del modelo Estado.
        :param municipios: variable que contiene todos los objetos del modelo Municipio.
        :param parroquias: variable que contiene todos los objetos del modelo Parroquia.
        :param obj_rlibro: variable que contiene el objeto del modelo Libro que coincide con el id dado.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    #estados = Estado.objects.all()
    obj_rlibro = Libros.objects.get(id=pk)
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    editoriales = Editorial.objects.all()
    sedes = Sede.objects.all()
    if request.method == 'POST':
        form_rlibro = FormLibros(request.POST, request.FILES, instance=obj_rlibro)
        if form_rlibro.is_valid():
            edit_rdirectivo = form_rlibro.save(commit=False)
            edit_rdirectivo.user = request.user.username
            edit_rdirectivo.save()
            x = datetime.datetime.now()
            #print "Fecha y Hora: "+str(x)
            reg_bitacora = Bitacora(
                accion="Actualización del libro '"+str(request.POST['cod_libro'])+"'...",
                usuario=request.user.username,
                fecha=x,)
            reg_bitacora.save()
            return HttpResponseRedirect('/libros/listar_libros')
    else:
        form_rlibro = FormLibros(instance=obj_rlibro)
    ctx = {'form_rlibro': form_rlibro, 'obj_rlibro': obj_rlibro, 'categorias': categorias, 'sedes': sedes, 'autores': autores, 'editoriales': editoriales}  # ctx = Contexto
    return render_to_response('libros/editar_libro.html', ctx, context_instance=RequestContext(request))


@login_required(login_url='/iniciar/login/')
def EliminarLibro(request, pk):
    """
        Función para eliminar una línea. Se usa 'context_object_name' para enviar el registro del modelo
        a la vista especificada.

        :param obj_rlibro: variable que contiene el objeto del modelo Libro que coincide con el id dado.
        :param x: variable que contiene la fecha y hora actual.
        :param reg_bitacora: variable que contiene la asignación de un nuevo registro al modelo Bitacora.
    """
    obj_rlibro = Libro.objects.get(id=pk)
    obj_rlibro.delete()
    x = datetime.datetime.now()
    #print "Fecha y Hora: "+str(x)
    reg_bitacora = Bitacora(
        accion="Eliminación de la línea '"+str(obj_rlibro.cod_libro)+"'...",
        usuario=request.user.username,
        fecha=x,)
    reg_bitacora.save()
    return HttpResponseRedirect('/libro/listar_libros')


#@login_required(login_url='/iniciar/login/')
#def FormReporteLibro(request):
#    """
#    Función para generar una vista para la selección de una línea de moto taxis específica. Se usa 'context_object_name' para enviar el registro del modelo
#    a la vista especificada.
#    """
#    listar_libros = Libro.objects.all()
#    ctx = {'listar_libros': listar_libros}  # ctx = Contexto
#    return render_to_response('libro/reporte_libro.html', ctx, context_instance=RequestContext(request))
#
#
#@login_required(login_url='/iniciar/login/')
#def ReporteLibro(request, libro):
#    """
#    Función para generar un reporte en pdf de los agremiados de una línea seleccionada.
#    """
#
#    LIBRO = libro
#
#    #print LIBRO
#
#    fecha = time.strftime("%d/%m/%Y")
#
#    hora = time.strftime("%I:%M %p")
#
#    fecha = str(fecha)+" "+str(hora)
#
#    consulta_agremiados = FichaPersonal.objects.filter(nom_libro=LIBRO)
#
#    consulta_libro = Libro.objects.filter(id=LIBRO)
#
#    archivo, nombre_archivo = report_libro.gen_res_libro(consulta_agremiados, fecha, consulta_libro)
#
#    response = HttpResponse(archivo.read(), content_type='application/pdf')
#    response['Content-Disposition'] = 'inline; filename="'+nombre_archivo.encode("UTF-8").decode("UTF-8")+'.pdf"'
#    return response


#======================================================================================
# Función para cargar los datos de un agremiado según su cédula
#======================================================================================
#@login_required(login_url='/iniciar/login/')
#def BuscarAgremiado(request):
#    """
#        Función para consultar los datos de un agremiado por su cédula.
#    """
#    cedula = request.GET['cedula']
#    agremiados = FichaPersonal.objects.filter(cedula=cedula)
#    data = serializers.serialize('json', agremiados, fields=('nacionalidad', 'cedula', 'p_nombre', 'p_apellido', 'estado', 'municipio', 'tlf_movil'))
#    return HttpResponse(data, content_type='application/json')
