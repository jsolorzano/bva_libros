# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_autor', models.CharField(unique=True, max_length=15, verbose_name=b'C\xc3\xb3digo del autor')),
                ('autor', models.CharField(max_length=200, verbose_name=b'Autor')),
                ('fecha_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='user_create',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='user_update',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
