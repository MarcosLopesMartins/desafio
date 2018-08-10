# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from verificar_nome import verificar_nome
from .models import Paciente

def test_retorna_falso_quando_nome_nao_eh_valido(self):
    nome = "Frase que não é um pangrama"
        
    nome_eh_valido = verificar_nome(nome)
        
    self.assertFalse(nome_eh_valido)


