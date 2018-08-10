# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Paciente, Invalidos

import django_filters

#
#----------------------------------------------
class PacienteFilter(django_filters.FilterSet):
    """ Finalidade: Disponibilizar opção de pesquisa
        para buscar determinados nomes"""
#----------------------------------------
#
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Paciente
        fields = ['nome']
#
#-----------------------------------------------
class InvalidosFilter(django_filters.FilterSet):
    """ Finalidade: Disponibilizar opção de pesquisa
        para buscar determinados nomes inválidos"""
#--------------------------------------------------
#
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Invalidos
        fields = ['nome']
