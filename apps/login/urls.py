from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from .views import login_view, logout_view, ProcesoUser, ListarUsuarios


"""
    Urls a la plantilla de inicio de sesion
"""
urlpatterns = patterns('',
                       url(r'^$', login_view, name='vista_login'),
                       url(r'^login/$', login_view, name='vista_login_enlace'),
                       url(r'^logout/$', logout_view, name='logout_view'),
                       url(r'^listar_usuarios/$', ListarUsuarios.as_view(), name='listar_usuarios'),
                       url(r'^nuevo_usuario/$', ProcesoUser.as_view(), name='nuevousuario'),
                       #url(r'^nuevo_usuario/$', RegistrarseUsuario.as_view(), name="nuevo_usuario",),
)
