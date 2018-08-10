# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db.models import Q

import string

from .models import Paciente

import .funcoes

#->

class PacienteModelTests(TestCase):

    def test_retorna_falso_quando_nome_nao_eh_valido(self):
        #nome = unicode("Marcos Lopes Martins")
        nome = unicode("Marco$ Lope$ Martin$")
        
        #nome_eh_valido = verificar_nome(nome)
        #self.assertTrue(nome_eh_valido)

        nome_eh_valido = Paciente(nome)
        self.assertIs(nome_eh_valido.verificar_nome(), True)

