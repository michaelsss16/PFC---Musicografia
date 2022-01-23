# Código de inicialização para o programa 
#Importações
import json
from Views.PaginaInicial  import *
with open('configuracoes.json') as file:
    config = json.load(file)
def Main():
    PaginaInicial()

Main()