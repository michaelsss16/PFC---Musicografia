# Página inicial do projeto
# Importações
import webbrowser 
import os 

from Views.PaginaConfiguracoes import *
from Views.PaginaExecucao import *

def PaginaInicial():
	Pulsar(buzzer)
	AtivarMotores(CELAVAZIA)
	Imprimir("Página inicial")
	opcao1 = '-1'
	while opcao1 != 0:
		opcao1 = EscolherComando([0, 1, 9, 10], OPCOESPAGINAINICIAL)

		if(opcao1 == 1):
			PaginaExecucao()
		elif(opcao1 == 9):
			PaginaConfiguracoes()
		elif(opcao1 == 10):
			Imprimir("Abrindo navegador...")
			webbrowser.open('file://' + os.path.realpath('../README.html'))
		elif(opcao1 == 0):
			Imprimir("Fim do programa")
			AtivarMotores(CELAVAZIA)
			Pulsar(buzzer, 1, 1, 0.5)
			exit()
			return 

