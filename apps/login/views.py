# -*- coding: utf-8 -*-
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
import hashlib
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages  # Metodo para la validacion de los campos
from apps.login.forms import LoginForm, UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from .models import PerfilesUsuario, User
from django.contrib.auth.models import User, Group
from django.db import connection, transaction # Cursor de django
import datetime
import json
from django.core import serializers
from passlib.hash import django_pbkdf2_sha256 as handler # Proceso para encriptar las contrasena


def login_view(request):
    """ Vista basada en Metodos o funciones: (`Ingresar`)
    Donde validamos que el usuario y la contraseña del mismo son validos de lo contrario se emite un mensaje.
    """
    mensaje = ""

    if request.user.is_authenticated():
        return HttpResponseRedirect('/menu/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "Usuario y/o Contraseña incorrecto"
        form = LoginForm()
        ctx = {'form': form, 'mensaje': mensaje}
        return render_to_response('login/login.html', ctx, context_instance=RequestContext(request))


class ProcesoUser(CreateView):
    """ Vista basada en clase: ('Registrar')
    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    """
    template_name = 'login/nuevo_usuario.html'
    model = User
    form_class = UserForm

    def post(self, request, *args, **kwargs):
       username = self.request.POST.get('username')
       password = handler.encrypt(self.request.POST.get('password'))
       email = self.request.POST.get('email')
       first_name = self.request.POST.get('first_name')
       last_name = self.request.POST.get('last_name')
       grupo = self.request.POST.get('grupo')
       accion = self.request.POST.get('accion')

       #print "USUARIO: ",accion
       # Bloque para la busqueda de usuario con contrasena y poder ser comparada con la db
       if accion == "buscar":
            print "PASO POR VERIFICAR"
            username = self.request.POST.get('id_fis')
            password = self.request.POST.get('password')
            password_f = self.request.POST.get('password_f')
            clave = handler.encrypt(password)

            print "ID usuario: ",username
            print "CLAVE: ",password

            usuario = authenticate(username=username, password=password_f)
            if not usuario:
                return HttpResponse('no_existe')
            else:
                print "Ya existe"

                # Query para permitir la actualizacion de la clave del fiscal
                query = User.objects.all()
                obj = query.filter(username=username)
                obj.update(
                    password = clave,
                    is_staff = True,
                )
                logout(request)
                return HttpResponseRedirect('/')


       elif accion == "guardar":
            print "Existe"
            existe = User.objects.filter(username = username).exists()
            if existe:
                return HttpResponse('existe')
            else:
                #print "ES por GUARDAR"
                if str(self.request.POST.get('is_active')) == '1':
                    status = True
                else:
                    status = False

                reg_obj = User(
                     username=username,
                     password=password,
                     last_login='2015-05-22 12:54:43.001975-04:30',
                     is_superuser='FALSE',
                     is_staff='FALSE',
                     is_active=status,
                     first_name=first_name,
                     last_name=last_name,
                     email=email,
                     date_joined='2015-05-22 12:54:43.001975-04:30',
                 )
                reg_obj.save()
                
                # Se captura id del grupo asociado a los fiscales y el id del nuevo fiscal registrado en usuario
                #id_group = Group.objects.filter(name='sistematizador')[0].id
                id_user = User.objects.filter(email = email)[0].id
                cursor = connection.cursor()
                cursor.execute("INSERT INTO auth_user_groups(user_id, group_id) VALUES ("+str(id_user)+", "+str(grupo)+")")
                
                return HttpResponse('exito')
        
       elif accion == "editar":
            pk = self.request.POST.get('valor')
            print "ESTATUS: ",self.request.POST.get('is_active')
            if str(self.request.POST.get('is_active')) == '1':
                status = True
                print "PASO POR 1"
            else:
                status = False
                print "PASO POR 2"
                
            # Query de actualizacion
            query = User.objects.all()
            obj = query.filter(id=pk)
            print "HOLA: ",obj
            obj.update(
                username=username,
                password=password,
                last_login='2015-05-22 12:54:43.001975-04:30',
                is_superuser='FALSE',
                is_staff=False,
                is_active=status,
                first_name=first_name,
                last_name=last_name,
                email=email,
                date_joined='2015-05-22 12:54:43.001975-04:30',
            )
            return HttpResponse('actualizar')
    
       return HttpResponseRedirect('/usuarios/listar_usuarios')
    
    def get_context_data(self, **kwargs):
        
        cursor = connection.cursor()
        cursor.execute("SELECT a.id, a.email, a.username, a.first_name, a.last_name, a.is_active,c.name FROM auth_user a INNER JOIN auth_user_groups au ON au.user_id = a.id INNER JOIN auth_group c ON c.id = au.group_id ORDER BY c.name ASC")
        data = cursor.fetchall()
        # print "LISTA: ",data
        context = {
            'listar_usuarios': data,
            'grupo': Group.objects.all().order_by('id'),
            }
        return context

# Vista para la lista de usuarios
class ListarUsuarios(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    :param paginate_by: Genera la paginacion de los registros en base a la cantidad definida.
    """
    model = User
    template_name = 'login/lista_usuarios.html'
    # context_object_name = "listar_usuarios"
    # paginate_by = 10
    
    def get_context_data(self, **kwargs):
        cursor = connection.cursor()
        user_lista = cursor.execute("SELECT a.id, a.email, a.username, a.first_name, a.last_name, a.is_active,au.group_id,c.name FROM auth_user a INNER JOIN auth_user_groups au ON au.user_id = a.id INNER JOIN auth_group c ON c.id = au.group_id")
        
        context = {
            'listar_usuarios': user_lista,
            'grupo': Group.objects.all().order_by('id'),
            }
        return context
    

def logout_view(request):
    print 'fsfdffsfs'
    """ metodo que cierra la sesion y redirecciona al usuario a la pagina de inicio.
    """
    logout(request)
    return HttpResponseRedirect('/')
