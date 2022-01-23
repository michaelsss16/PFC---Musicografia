# Página inicial do projeto
# Importações
from Views.PaginaConfiguracoes import *

def PaginaInicial():
    Imprimir("Página inicial")
    opcao1 = '-1'
    opcao1 = input(Imprimir("1- Carregar partitura\n 9- Configurações\n 0- Sair do programa\n"))
    if(opcao1 == '9'):
        PaginaConfiguracoes()
    if(opcao1 == '0'):
        Imprimir("Fim do programa")



    
