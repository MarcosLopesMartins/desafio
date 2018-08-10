# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from .models import Paciente, Invalidos

#
class PacienteSerializer(serializers.ModelSerializer):
    """ Finalidade: Disponibilizar opção de pesquisa
        dos pacientes para buscar determinados nomes"""
#------------------------------------------------------
#
    class Meta:

        model = Paciente
        fields = '__all__'

class InvalidosSerializer(serializers.ModelSerializer):
    """ Finalidade: Disponibilizar opção de pesquisa de 
        nomes inválidos dos pacientes para buscar 
        determinados nomes"""
#----------------------------
#
    class Meta:

        model = Invalidos
        fields = '__all__'

