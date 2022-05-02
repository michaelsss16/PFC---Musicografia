import json
from Views.PaginaConfiguracoes import *
from Placa.Placa import *
from Utils.Constantes import *
from pyfirmata import ArduinoMega, util
import time                     

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

# Função principal da página de execução da partitura em arquivo
def PaginaExecucao():
	dic = DicionarioBraille()
	Imprimir(Constantes['PaginaDeExecucao']['MensagemDeInicializacao'])
	with open('./PartituraInicial.txt', encoding='utf-8', mode='r') as file:
		texto = file.read()
		file.close()
	tamanhoDaPagina = len(texto)
	nota = 0
	while(nota != tamanhoDaPagina):
		cela = TratarEntrada(texto[nota], dic)
		Imprimir(cela)
		AtivarMotores(cela)
		nota = nota + AvancoOuRecuoPressionado(botaoAvanco, botaoRecuo)

	Imprimir(Constantes['PaginaDeExecucao']['MensagemDeFinalizacao'])
	Pulsar(buzzer, 1)
	AtivarMotores(CELAVAZIA)
	return