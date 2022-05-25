import json
import time                     
import os

from Views.PaginaConfiguracoes import *
from Placa.Placa import *
from Utils.Constantes import *
from Utils.Util import *
from pyfirmata import ArduinoMega, util

partituraSelecionada = './Partituras/PartituraInicial.txt'

# Definição das funções utilizadas para acesso ao dicionário braille e conversão dos pontos para cela matricial
def DicionarioBraille():
	file = open('BrailleDictionary.json', encoding='utf-8', mode='r') 
	dic = json.load(file)
	file.close()
	return dic

def ConverterParaCela(letra, dicionario):
	cela = [0, 0, 0, 0, 0, 0]
	try:
		numero = dicionario[letra.lower()][0]
		binario = bin(numero)
		vetor = [int(d) for d in str(bin(numero))[2:]]
		vetor = vetor[::-1]
		for d in range(len(vetor)):
			cela[d] = vetor[d]
		return cela
	except:
		#Imprimir("Erro na definição da cela. Verifique o documento de partitura")
		return CELAVAZIA

# Função para saídas específicas para casos especiais de entrada do documento de partitura
def TratarEntrada(letra, dicionario):
	cela = ConverterParaCela(letra, dicionario)
	if(letra == '\n'):
		 Pulsar(buzzer, 1, 1, 0.1) 
		 Imprimir("Quebra de linha")
	return cela

def IniciarReproducao():
	global partituraSelecionada
	dic = DicionarioBraille()
	with open(partituraSelecionada, encoding='utf-8', mode='r') as file:
		texto = file.read()
		file.close()
	tamanhoDaPagina = len(texto)
	nota = 0
	while(nota != tamanhoDaPagina):
		cela = TratarEntrada(texto[nota], dic)
		Imprimir(cela)
		  
		AtivarMotores(cela)
		passo = AvancoOuRecuoPressionado(botaoAvanco, botaoRecuo, botaoReset)
		if passo == 0:
			nota = 0
		if passo == 'END':
			break
		nota = nota + passo

	Imprimir(Constantes['PaginaDeExecucao']['MensagemDeFinalizacao'])
	Pulsar(buzzer, 1)
	AtivarMotores(CELAVAZIA)
	return

def EscolherPartitura():
	global partituraSelecionada
	cont = 0
	pasta = './Partituras'
	Imprimir("Partituras disponíveis: ")
	for diretorio, subpastas, arquivos in os.walk(pasta):
		size = len(arquivos)
		for arquivo in arquivos:
			Imprimir(str(cont) + '- '+ arquivo)
			cont = cont +1

	escolha = int(input(Imprimir("Digite o número correspondente a sua escolha: ")))
	if escolha >= size:
		Imprimir("Valor inválido")
	else:
		Imprimir("Partitura escolhida: " + arquivos[escolha])
		partituraSelecionada = './Partituras/'+ arquivos[escolha]

	return 

# Função principal da página de execução da partitura em arquivo
def PaginaExecucao():
	opcao2 = -1
	Imprimir("Página de execução de partitura")
	while opcao2 != 0:
		opcao2 = EscolherComando([0, 1, 2, 10], OPCOESPAGINAEXECUCAO)
		if opcao2 == 0:
			return 
		if  opcao2 == 1:
			IniciarReproducao()

		if opcao2 == 2:
			EscolherPartitura()

		if opcao2 == 10:
			Imprimir(TEXTOAJUDAEXECUCAO)
