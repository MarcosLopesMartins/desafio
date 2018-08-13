# desafio
API em Python com Framework Django Rest

Python com Django e Django Rest

Banco de Dados: Postgres

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'widget_tweaks',
    'rest',
]

REST_FRAMEWORK = {
    
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

A carga do dataset para testes está em: rest/funcoes.py

Views: 1. carga do dataset
       2. Pesquisas (todos os nomes)
       3. Pesquisa apenas nomes inválidos
       
Snapshots: home.png, search.png e check.png

