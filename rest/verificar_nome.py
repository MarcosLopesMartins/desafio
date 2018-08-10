# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import string

def verificar_nome(nome):
    for letra in string.ascii_lowercase:
        if letra not in nome.lower():
            return False
    return True
