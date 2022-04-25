# Desenvolvimento de uma função que recebe uma letramaiúscula ou minúscula e retorna um vetor contendo seis posições indicativas para a cela braille 
import json 

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



entrada = "Inicio"
dic = DicionarioBraille()
while entrada!= "sair":
	entrada = input("Letra: ")
	print(ConverterParaCela(entrada, dic))
	print(dic[entrada][1])

