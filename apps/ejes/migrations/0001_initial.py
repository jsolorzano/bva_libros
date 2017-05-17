# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Eje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_eje', models.CharField(unique=True, max_length=15, verbose_name=b'C\xc3\xb3digo del eje')),
                ('eje', models.CharField(max_length=200, verbose_name=b'Eje')),
                ('fecha_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_update', models.DateTimeField(auto_now=True, null=True)),
                ('user_create', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_update', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
