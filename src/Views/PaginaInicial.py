# Página inicial do projeto
# Importações
import webbrowser 
import os 

from Views.PaginaConfiguracoes import *
from Views.PaginaExecucao import *
from Views.PaginaEscrita import *
from Views.PaginaControleDireto import *

def PaginaInicial():
	Pulsar(buzzer)
	AtivarMotores(CELAVAZIA)
	opcao1 = '-1'
	while opcao1 != 0:
		Imprimir("Página inicial")
		opcao1 = EscolherComando([0, 1, 2, 3, 8, 9, 10], OPCOESPAGINAINICIAL)

		if(opcao1 == 1):
			PaginaExecucao()
		elif opcao1 == 2:
			PaginaEscrita()
		elif opcao1 == 3:
			PaginaControleDireto()
		elif(opcao1 == 8):
			PaginaConfiguracoes()
		elif(opcao1 == 9):
			Imprimir("Abrindo navegador...")
			webbrowser.open('file://' + os.path.realpath('../README.html'))
		elif(opcao1 == 10):
			Imprimir(TEXTOAJUDAPAGINAINICIAL)
		elif(opcao1 == 0):
			Imprimir("Fim do programa")
			AtivarMotores(CELAVAZIA)
			Pulsar(buzzer, 1, 1, 0.5)
			exit()
			return 

