# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest.models import Paciente, Invalidos
from rest.funcoes import carga_dataset

from .filters import PacienteFilter, InvalidosFilter

from .serializers import PacienteSerializer
from rest_framework import generics, viewsets

#->

from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_condition import Or
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

#from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication

import string

#------------------
def carga(request):
    """ Finalidade: Ler o dataset para carregar o Banco de Dados
        e apontar nomes inválidos"""
#-----------------------------------    
#
    mensagem = carga_dataset(None)
    #if mensagem:
    #    raise ValueError(mensagem)

    paciente_list = Paciente.objects.all()
    paciente_filter = PacienteFilter(request.GET, queryset=paciente_list)
    return render(request, 'rest/carga_list.html', {'filter': paciente_filter})
#
#-------------------
def search(request):
    """ Finalidade: Listar todos os nomes
        e disponibilizar opção de pesquisa"""
#--------------------------------------------
#
    paciente_list = Paciente.objects.all()
    paciente_filter = PacienteFilter(request.GET, queryset=paciente_list)
    return render(request, 'rest/paciente_list.html', {'filter': paciente_filter})
#
#----------------------
def invalidos(request):
    """ Finalidade: Listar todos os nomes inválidos
        e disponibilizar opção de pesquisa"""
#--------------------------------------------
#
    invalidos_list = Invalidos.objects.all()
    invalidos_filter = InvalidosFilter(request.GET, queryset=invalidos_list)
    return render(request, 'rest/invalidos.html', {'filter': invalidos_filter})

