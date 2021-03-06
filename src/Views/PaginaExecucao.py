import json
import time                     
import os

from Views.PaginaConfiguracoes import *
from Placa.Placa import *
from Utils.Constantes import *
from Utils.Util import *
from pyfirmata import ArduinoMega, util

# Variáveis globais
global partituraSelecionada 
partituraSelecionada = Configuracoes['Partitura']['Arquivo']

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


def ApresentarInformacoesNota(nota, dicionario):
	try:
		if Configuracoes['Interface']['Musicografia']: Imprimir(dicionario[str(nota)][1])
		if Configuracoes['Interface']['Alfabeto']: Imprimir(dicionario[str(nota)][0])
	except:
		Imprimir(" ")

def ConverterParaCela(valor):
	cela = [0, 0, 0, 0, 0, 0]
	try:
		binario = bin(int(valor))
		vetor = [int(d) for d in str(bin(valor))[2:]]
		vetor = vetor[::-1]
		for d in range(len(vetor)):
			cela[d] = vetor[d]
		if Configuracoes['Interface']['Matriz']: Imprimir(cela)
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
		Configuracoes['Partitura']['Arquivo'] =  partituraSelecionada 
		with open('Configuracoes.json', 'w') as file:
			json.dump(Configuracoes, file, indent=4)

		try:
			with open(partituraSelecionada, encoding='utf-8', mode='r') as file:
				arquivo = json.load(file)
				file.close()
			ApresentarInformacoesPartitura(arquivo)
		except:
			Imprimir("Ocorreu um problema ao tentar carregar o arquivo de partitura")
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
def IniciarReproducao(modo, bpm = 60):
	global partituraSelecionada
	notaAnterior = -1
	Dicionario = RetornarDicionario()
	with open(partituraSelecionada, encoding='utf-8', mode='r') as file:
		arquivo = json.load(file)
		file.close()

	if Configuracoes['Interface']['InformacoesPartitura']: ApresentarInformacoesPartitura(arquivo)

# Preparo do arquivo de composição 
	composicao = arquivo['Data']
	tamanhoTotal = 0
	tamanhoCompassos = [0]
	for compasso in range(len(composicao)):
		tamanhoTotal = tamanhoTotal + len(composicao[compasso])
		tamanhoCompassos.append(len(composicao[compasso]))
	vetorFinais = RetornarFinais(tamanhoCompassos)

# Opções de apresentação de informações da partitura e metrônomo 
	if Configuracoes['Interface']['Metronomo']:
		Imprimir('Pressione qualquer botão da placa para iniciar a reprodução do metrônomo')
		AguardarQualquerBotaoSerPressionado()

		if modo == 'manual':
			Metronomo(arquivo['BPM'])
		if modo == 'automatico':
			Metronomo(bpm, 3)

	Imprimir("Pressione qualquer botão da placa para iniciar a reprodução")
	AguardarQualquerBotaoSerPressionado()

	#Navegando na execução da partitura
	notaLinear= 1
	notaCompasso = 0
	compasso = 0

	while notaLinear!= tamanhoTotal+1:
		if notaCompasso == 0 and compasso>=0 and Configuracoes['Interface']['BipCompasso']:  
			Pulsar(buzzer, 1, 1, 0.1)
			if Configuracoes['Interface']['MensagemCompasso']: Imprimir('Compasso número '+ str(compasso+1))

		nota = composicao[compasso][notaCompasso]
		if nota == notaAnterior and Configuracoes['Interface']['ResetCela']:
			AtivarMotores(CELAVAZIA)
			time.sleep(0.25)
		AtivarMotores(ConverterParaCela(nota))
		ApresentarInformacoesNota(nota, Dicionario)
		notaAnterior = nota

		if modo == 'automatico':
			time.sleep(60/bpm)
			notaLinear = notaLinear+1
			posicaoECompasso = RetornarCompassoENota(vetorFinais, notaLinear)
			compasso = posicaoECompasso[0]
			notaCompasso = posicaoECompasso[1]

		if modo == 'manual':
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
		opcao2 = EscolherComando([0, 1, 2, 3, 10], OPCOESPAGINAEXECUCAO)
		if opcao2 == 0:
			return 
		if  opcao2 == 1:
			IniciarReproducao('manual')

		if opcao2 == 2:
			bpm = RetornarBpm()
			IniciarReproducao('automatico', bpm)
		if opcao2 == 3:
			EscolherPartitura()

		if opcao2 == 10:
			Imprimir(TEXTOAJUDAEXECUCAO)

