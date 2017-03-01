from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
import settings

#router = DefaultRouter()
#router.register(r'registro', FichaPersonalViewSet)
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'fumtea.views.home', name='home'),
                       url(r'^iniciar/', include('apps.login.urls')),
                       url(r'^libros/', include('apps.libros.urls')),
                       # Url direccion a la URL login
                       url(r'^$', 'apps.libros.views.home', name='home'),  # Url direccion a la URL login
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^/', include(router.urls)),
                       url(r'^categorias/', include('apps.categorias.urls')),
                       url(r'^autores/', include('apps.autores.urls')),
                       url(r'^editoriales/', include('apps.editoriales.urls')),
                       url(r'^ejes/', include('apps.ejes.urls')),
                       url(r'^sedes/', include('apps.sedes.urls')),
                       url(r'^usuarios/', include('apps.login.urls')),
                       url(r'^bitacora/', include('apps.bitacora.urls')),
                       url(r'^foto/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'^reporte/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_PDF}),
                       )
