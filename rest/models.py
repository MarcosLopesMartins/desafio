# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Q


#----------------------------
class Paciente(models.Model):
    """ Finalidade: Armazenar os nomes dos
        dos pacientes originados de um dataset"""
#------------------------------------------------
#
    nome = models.CharField(max_length=200)

    class Meta:

        db_table = 'paciente'
        ordering = ['nome']

    def __str__(self):
        return self.nome

#-----------------------------
class Invalidos(models.Model):
    """ Finalidade: Armazenar os nomes inválidos dos
        dos pacientes para pesquisa"""
#-------------------------------------
#
    nome = models.CharField(max_length=200)

    class Meta:

        db_table = 'invalidos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

