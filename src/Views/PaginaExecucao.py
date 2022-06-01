import json
import time                     
import os

from Views.PaginaConfiguracoes import *
from Placa.Placa import *
from Utils.Constantes import *
from Utils.Util import *
from pyfirmata import ArduinoMega, util

# Variáveis globais
partituraSelecionada = './Partituras/PartituraInicial.json'

def ApresentarInformacoesPartitura(arquivo):
	try:
		if Configuracoes['Interface']['InformacoesPartitura']:
			print('Título: '+arquivo['Titulo'])
			print('Autor: '+arquivo['Autor'])
			print('BPM: '+str(arquivo['BPM']))
	except:
		print('Não foi possível encontrar as informações da partitura selecionada')
# Definição das funções utilizadas para acesso ao dicionário braille e conversão dos pontos para cela matricial
def RetornarDicionario():
	file = open('DicionarioCombinacoes.json', encoding='utf-8', mode='r') 
	dic = json.load(file)
	file.close()
	return dic


def AprsentarInformacoesNota(nota, dicionario):
	try:
		Imprimir(dicionario[str(nota)][0])
	except:
		return

def ConverterParaCela(valor):
	cela = [0, 0, 0, 0, 0, 0]
	try:
		binario = bin(int(valor))
		vetor = [int(d) for d in str(bin(valor))[2:]]
		vetor = vetor[::-1]
		for d in range(len(vetor)):
			cela[d] = vetor[d]
		if Configuracoes:
			print(cela)
		return cela
	except:
		#Imprimir("Erro na definição da cela. Verifique o documento de partitura")
		return CELAVAZIA

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

#Funções auxiliares de navegação na matriz da composição
def RetornarFinais(tamanhoCompassos):
	somatorio = 0
	finais = [0]
	for i in range(1, len(tamanhoCompassos)):
		finais.append(somatorio + tamanhoCompassos[i])
		somatorio = somatorio + tamanhoCompassos[i]
	return finais

def RetornarCompasso(finais, nota):
	compasso = 0
	for i in range(len(finais)):
		if nota <= finais[i]:
			compasso = i
			break
	return compasso-1

def RetornarCompassoENota(vetorFinais, nota):
	if nota > vetorFinais[-1]:
		return [-1, -1]

	compasso = RetornarCompasso(vetorFinais, nota)
	notaNoCompasso = nota - vetorFinais[compasso]-1
	return [compasso, notaNoCompasso]

def ProximoCompasso(vetorFinais, nota):
	compasso = RetornarCompasso(vetorFinais, nota)
	if compasso == (len(vetorFinais)-2):
		Imprimir('Último compasso')
		return 'end'
	Imprimir('Próximo compasso')
	return [compasso+1, vetorFinais[compasso+1]+1]

def CompassoAnterior(vetorFinais, nota):
	vetorPosicao = RetornarCompassoENota(vetorFinais, nota)
	if vetorPosicao[0]==0:
		Imprimir('Início da partitura')
		return [0, 1]
	elif vetorPosicao[1]==0:
		Imprimir('Compasso anterior')
		return [vetorPosicao[0]-1, 1]
	else:
		Imprimir('Início do compasso')
		return [vetorPosicao[0], vetorFinais[vetorPosicao[0]]+1]

# Função principal para a reprodução 
def IniciarReproducao():
	global partituraSelecionada
	Dicionario = RetornarDicionario()
	with open(partituraSelecionada, encoding='utf-8', mode='r') as file:
		arquivo = json.load(file)
		file.close()
	ApresentarInformacoesPartitura(arquivo)
	composicao = arquivo['Data']
	tamanhoTotal = 0
	tamanhoCompassos = [0]
	for compasso in range(len(composicao)):
		tamanhoTotal = tamanhoTotal + len(composicao[compasso])
		tamanhoCompassos.append(len(composicao[compasso]))
	vetorFinais = RetornarFinais(tamanhoCompassos)

	#Navegando na execução da partitura
	notaLinear= 1
	notaCompasso = 0
	compasso = 0
	while notaLinear!= tamanhoTotal+1:
		AtivarMotores(ConverterParaCela(composicao[compasso][notaCompasso]))
		AprsentarInformacoesNota(composicao[compasso][notaCompasso], Dicionario)
		operacao = AvancoOuRecuoPressionado(botaoAvanco, botaoRecuo, botaoReset)
		if operacao == 1:
			notaLinear = notaLinear+1
			posicaoECompasso = RetornarCompassoENota(vetorFinais, notaLinear)
			compasso = posicaoECompasso[0]
			notaCompasso = posicaoECompasso[1]
		if operacao == -1:
			if notaLinear != 1:
				notaLinear = notaLinear-1
			posicaoECompasso = RetornarCompassoENota(vetorFinais, notaLinear)
			compasso = posicaoECompasso[0]
			notaCompasso = posicaoECompasso[1]
		if operacao == 0:
			cnota= CompassoAnterior(vetorFinais, notaLinear)
			compasso = cnota[0]
			notaLinear = cnota[1]
			retorno = RetornarCompassoENota(vetorFinais, notaLinear)
			notaCompasso = retorno[1]
			
		if operacao == 'finalizar':
			break
		if operacao == 'end':
			cnota= ProximoCompasso(vetorFinais, notaLinear)
			if cnota == 'end':
				break
			compasso = cnota[0]
			notaLinear = cnota[1]
			retorno = RetornarCompassoENota(vetorFinais, notaLinear)
			notaCompasso = retorno[1]

	Imprimir("Fim da execução da partitura")
	Pulsar(buzzer, 1)
	AtivarMotores(CELAVAZIA)
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

