# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db.models import Q

from .models import Paciente, Invalidos

#---------------------------
def carga_dataset(mensagem):
    """ Finalidade: Ler o dataset para carregar o Banco de Dados
        e apontar nomes inválidos"""
#-----------------------------------

    mensagem = u'Apenas testando...'
    return mensagem

    import csv
    import string

#-> Definição das variaveis necessarias
    pid = 0
#
#-> Lendo o CSV para a carregar a tabela
#
    try:
        f = open('//home/marcos/workspace/desafio/patients.csv', 'rb')
        csv_file = csv.reader(f)
    except:
        mensagem = u'Ops!!! CSV não encontrado. Carga do dataset não foi efetuada, verifique...'
        return mensagem
#
#-> Limpar dados antigos
#
    if csv_file:
        chk = Paciente.objects.all()
        if chk:
            Paciente.objects.all().delete()
        chk = Invalidos.objects.all()
        if chk:    
            Invalidos.objects.all().delete()
#        except:
#            mensagem = u'Ops!!! Carga do dataset não foi realizada. Verifique seu conteudo...'
#            return mensagem
#            pass

    for row in csv_file:
        nome = str(row).strip('[]')
        nome = str(nome).strip("'")

        pid += 1
        reg = Paciente()
        reg.nome = nome
        reg.save()
#
#-> Checar nome inválido
#
        nome = reg.nome.replace(' ','')
        for letra in nome.lower():
            if letra not in string.ascii_lowercase:
                regg = Invalidos()
                regg.nome = nome
                regg.save()
                break

    f.close()

    if pid > 0:
        print pid
        print ('Ok!!! Carga do dataset efetuada com sucesso...')
    else:
        mensagem = u'Ops!!! Carga do dataset não foi efetuada, verifique...'
#---------------------------------------------------------------------------

    return mensagem
#
#------------------

