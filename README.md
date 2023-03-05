# desafio-credit

Repositório para criação de uma API simples para cartão de crédito.

# Fazer a criação do ambiente virtual definindo a versão do python
virtualenv venv --python=/usr/bin/python3.10

# Ativar ambiente virtual
source venv/bin/activate

# Instalar Django e DRF
pip install django djangorestframework

# Instalar biblioteca necessária para verificação do cartão
pip install git+https://github.com/maistodos/python-creditcard.git@main

# Instalar biblioteca para fazer criptografia
pip install cryptography

# Criar um novo projeto chamado credit
django-admin startproject credit

# Inicializar projeto e fazer migrations iniciais
python3 manage.py startapp api

python3 manage.py migrate

# Comando para rodar o server
python3 manage.py runserver

