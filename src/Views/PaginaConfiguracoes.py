#Importações
import json 
from Utils.Util import *
from Utils.Constantes import *

def AlterarConfiguracao(chave1, chave2,textoParametro, ehBinario =True, valor = 1, mensagemApoio = 'Alteração executada com sucesso'):
	if ehBinario:
		if Configuracoes[chave1][chave2]:
			Imprimir("Desativando "+ textoParametro)
			Configuracoes[chave1][chave2] = False
		elif Configuracoes[chave1][chave2]==False:
			Imprimir("Ativando"+ textoParametro)			
			Configuracoes[chave1][chave2] = True

	else:
		Imprimir('Alterando valor da configuração' + textoParametro+ ' para '+ valor)
		Configuracoes[chave1][chave2] = valor
	with open('Configuracoes.json', 'w') as file:
		json.dump(Configuracoes, file, indent=4)


def PaginaConfiguracoes():
	Imprimir("Página de configurações")
	while True:
		opcao2 = EscolherComando([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19], OPCOESPAGINACONFIGURACOES )
		if opcao2 == 0:
			break
		if(opcao2 == 1):
			AlterarConfiguracao("Sintetizador",'Sintetizador', 'sintetizador de voz')
		if opcao2 == 2:
			AlterarConfiguracao('Interface', 'BipsBuzzer', 'bips da interface')
		if opcao2 ==  3:
			AlterarVozDoSintetizador()

		if opcao2 == 4:
			AlterarConfiguracao('Interface', 'Metronomo', 'metrônomo')
		if opcao2 == 5:
			AlterarConfiguracao('Interface', 'InformacoesPartitura', 'informações da partitura')
		if opcao2 == 6:
			AlterarConfiguracao('Interface', 'BipCompasso', 'bips do compasso')
		if opcao2 == 7:
			AlterarConfiguracao('Interface', 'MensagemCompasso', 'bips do compasso')
		if opcao2 == 8:
			AlterarConfiguracao('Interface', 'Musicografia', 'apresentação de dados musicográficos')
		if opcao2 == 9:
			AlterarConfiguracao('Interface', 'Alfabeto', 'apresentação de dados do alfabeto tradicional')
		if opcao2 == 10:
			AlterarConfiguracao('Interface', 'Matriz', 'apresentação da matriz de acionamento dos motores')
		if opcao2 == 11:
			AlterarConfiguracao('Interface', 'ResetCela', 'adição de espaço entre duas notas consecutivas idênticas durante a reprodução')

		if opcao2 == 18:
			try:
				escolha = input(Imprimir("Digite o número da porta que deseja atribuir para comunicação com a placa arduino:"))
				AlterarPortaDeComunicacao(escolha)
			except:
				Imprimir('O valor inserido não é válido')
		if(opcao2==19):
			with open('Configuracoes.json', 'w') as file:
				json.dump(ConfiguracaoPadrao, file, indent=4)
				file.close()
	return
		
