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
		return "Erro na definição da cela"

# Função principal da página de execução da partitura em arquivo
def PaginaExecucao():
	dic = DicionarioBraille()
	Imprimir(Constantes['PaginaDeExecucao']['MensagemDeInicializacao'])
	with open('./PartituraInicial.txt', encoding='utf-8', mode='r') as file:
		texto = file.readlines()
	for linha in texto:
		for nota in linha:
			AvancoOuRecuoPressionado(botaoAvanco, botaoRecuo)
			Imprimir(ConverterParaCela(nota, dic))
	Imprimir(Constantes['PaginaDeExecucao']['MensagemDeFinalizacao'])
	Pulsar(buzzer, 0.3)