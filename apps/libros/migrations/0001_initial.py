# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('editoriales', '0002_auto_20170208_1436'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autores', '0002_auto_20170208_1052'),
        ('categorias', '0001_initial'),
        ('sedes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_libro', models.CharField(max_length=15, unique=True, null=True, verbose_name=b'C\xc3\xb3digo de libro', blank=True)),
                ('titulo', models.CharField(max_length=200, null=True, verbose_name=b'T\xc3\xadtulo', blank=True)),
                ('fecha_pub', models.DateField(null=True, verbose_name=b'Fecha de Publicaci\xc3\xb3n', blank=True)),
                ('fecha_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('autor', models.ForeignKey(related_name='autor_libro', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_autor', to='autores.Autor', null=True)),
                ('categoria', models.ForeignKey(related_name='categoria_libro', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_categoria', to='categorias.Categoria', null=True)),
                ('editorial', models.ForeignKey(related_name='editorial_libro', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_editorial', to='editoriales.Editorial', null=True)),
                ('sede', models.ForeignKey(related_name='sede_libro', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_sede', to='sedes.Sede', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
