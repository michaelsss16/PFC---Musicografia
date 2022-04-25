# Página inicial do projeto
# Importações
import webbrowser 
import os 

from Views.PaginaConfiguracoes import *
from Views.PaginaExecucao import *

def PaginaInicial():
	Pulsar(buzzer)
	Imprimir("Página inicial")
	opcao1 = '-1'
	opcao1 = input(Imprimir("1- Iniciar execução\n 9- Configurações\n 10- Abrir documentação\n 0- Sair do programa\n"))
	if(opcao1 == '1'):
		PaginaExecucao()
	if(opcao1 == '9'):
		PaginaConfiguracoes()
	if(opcao1 == '10'):
		Imprimir("Abrindo navegador...")
		with open('../README.html', encoding='utf-8', mode='r') as file:
			filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
			file.close()
	if(opcao1 == '0'):
		Imprimir("Fim do programa")
		Pulsar(buzzer, 0.3)
		AvancoOuRecuoPressionado(botaoAvanco, botaoRecuo)
