from Views.PaginaConfiguracoes import *
from Views.PaginaExecucao import *
from Views.PaginaEscrita import *
from Placa.Placa import *
from Utils.Constantes import *
from Utils.Util import *
from pyfirmata import ArduinoMega, util

def EnviarComandos():
	maxAng = 90
	minAng = 0
	Imprimir('Digite 0 ou sair para finalizar.')
	dicionario = RetornarDicionario()
	entrada = ''
	cela = [0, 0, 0, 0, 0, 0]
	
	while (entrada != '0') and  (entrada !='sair'):
		AtivarMotores(cela)
		ApresentarInformacoesNota(obtemCodigo(entrada), dicionario)
		entrada = input()
		cela = [0, 0, 0, 0, 0, 0]
		for letra in entrada:
			if letra == 's': cela[2]=1
			if letra == 'd': cela[1]=1
			if letra == 'f': cela[0]=1
			if letra == 'j': cela[3]=1
			if letra == 'k': cela[4]=1
			if letra == 'l': cela[5]=1
		if Configuracoes['Interface']['Matriz']: Imprimir(cela)
	AtivarMotores([0, 0, 0, 0, 0, 0])

def PaginaControleDireto():
	opcao2 = -1
	Imprimir('Página de escrita direta para plataforma')
	while opcao2 != 0:
		opcao2 = EscolherComando([0, 1, 10], OPCAOESPAGINACONTROLEDIRETO)
		if opcao2 == 0:
			break
		elif opcao2 == 1:
			EnviarComandos()
		elif opcao2 == 10:
			Imprimir(TEXTOAJUDAPAGINACONTROLEDIRETO)
	Imprimir("Retornando para a  página inicial.")
	