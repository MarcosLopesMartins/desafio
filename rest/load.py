# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django import db

from .models import Paciente

import csv

#---------------------------------------

#-> Definição das variaveis necessarias
pid = 0

#-> Lendo o CSV para a carregar a tabela

try:
    f = open('//home/marcos/workspace/desafio/patients.csv', 'rb')
    csv_file = csv.reader(f)
except:
    raise ValueError('Ops!!! CSV não encontrado. Carga do dataset não foi efetuada, verifique...')

#
#-> Limpar dados antigos
Paciente.objects.all().delete()

if csv_file:
    try:
        Paciente.objects.all().delete()
    except:
        raise ValueError('Ops!!! Carga do dataset não foi realizada. Verifique seu conteudo...')

for row in csv_file:
    pid += 1
    reg = Pacientes()
    reg.nome = row
    reg.save()

f.close()

#---------------------------------------------------------------------------

if pid > 0:
    print pid
    print ('Ok!!! Carga do dataset efetuada com sucesso...')
else:
    raise ValueError('Ops!!! Carga do dataset não foi efetuada, verifique...')
#-----------------------------------------------------------------------------

main()


