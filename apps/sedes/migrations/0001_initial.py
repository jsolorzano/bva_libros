# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ejes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_sede', models.CharField(unique=True, max_length=15, verbose_name=b'C\xc3\xb3digo de sede')),
                ('sede', models.CharField(max_length=200, verbose_name=b'Sede')),
                ('descripcion', models.CharField(max_length=200, verbose_name=b'Descripci\xc3\xb3n')),
                ('fecha_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('eje', models.ForeignKey(related_name='eje_sede', on_delete=django.db.models.deletion.SET_NULL, to_field=b'cod_eje', to='ejes.Eje', null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
