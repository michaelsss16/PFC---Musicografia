import json
from Utils.Constantes import *
from Utils.Util import *

def DefinirBpmPartitura():
	val = input(Imprimir('Digite o valor do BPM ou 0 para iniciar a ajuda de definição.'))
	if val == '0':
		return RetornarBpm()
	else: 
		try:
			return int(val)
		except:
			Imprimir("O valor inserido não é válido. Utilizando valor padrão de 60 BPM.")
			return 60

def obtemCodigo(entrada):
	soma = 0
	for letra in entrada:
		if letra == 'f':
			soma+=1
		if letra == 'd':
			soma+=2
		if letra == 's':
			soma+=4
		if letra == 'j':
			soma+=8
		if letra == 'k':
			soma+=16
		if letra == 'l':
			soma+=32
	if soma >=64:
		return 0
	return soma

def trataEntrada(entrada):
	retorno = []
	array_entrada = entrada.split(' ')
	for sequencia in array_entrada:
		retorno.append(obtemCodigo(sequencia))
	return retorno

def IniciarLeitura():
	entrada = 0
	composicao = []
	print("Digite sair para encerrar a escrita")
	while True:
		entrada = input("entrada: ")
		if entrada == 'sair':
			break
		composicao.append(trataEntrada(entrada))
	
	print("Fim da aquisição de entradas")
	return composicao

# Função principal para a página de escrita de partituras 
def PaginaEscrita():
	opcao2 = 0
	arquivoJson ={
		'Titulo': 'Composicao sem titulo',
		'BPM': 180,
		'Autor': 'Desconhecido',
		'Data': []} 

	Imprimir("Página de escrita de partituras")
	opcao2 = EscolherComando([0, 1, 10], OPCOESPAGINAESCRITA)
	if opcao2 == 0:
		return 
	if opcao2 == 1:
		retorno = IniciarLeitura()
		opcao3 = EscolherComando([0, 1], ['0- Descartar rascunho', '1- Salvar composição'])
		if opcao3 ==  0:
			return 
		elif opcao3 == 1:
			nomeDoArquivo = input(Imprimir('Digite o nome do arquivo a ser salvo: '))
			arquivoJson['Titulo'] = input(Imprimir('Digite o título da composição: '))
			arquivoJson['Autor'] = input(Imprimir('Digite o autor da composição: '))
			arquivoJson['BPM'] = DefinirBpmPartitura()
			arquivoJson["Data"]= retorno
		with open('./Partituras/'+nomeDoArquivo+'.json', 'w') as file:
				json.dump(arquivoJson, file, indent=4)

	if opcao2 == 10:
		Imprimir(TEXTOAJUDAPAGINAEXECUCAO )
	return 
