# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [

#    url(r'^pacientes/$', views.PacienteList.as_view(), name='paciente-list'),
#    url(r'^paciente/(?P<pk>[0-9]+)/$', views.PacienteDetail.as_view(), name='paciente-detail'),

    url(r'^carga/$', views.carga, name='carga'),

    url(r'^search/$', views.search, name='search'),

    url(r'^invalidos/$', views.invalidos, name='invalidos'),

]
