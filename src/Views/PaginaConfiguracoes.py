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
	opcao2 = EscolherComando([0, 1, 2, 3, 8, 9], OPCOESPAGINACONFIGURACOES )
	if opcao2 == '0':
		return 
	if(opcao2 == 1):
		AlterarConfiguracao("Sintetizador",'Sintetizador', 'sintetizador de voz')
	if opcao2 == 2:
		AlterarConfiguracao('Interface', 'BipsBuzzer', 'bips da interface')
	if opcao2 ==  3:
		AlterarVozDoSintetizador()

	if opcao2 == 8:
		escolha = input(Imprimir("Digite o número da porta que deseja atribuir para comunicação com a placa arduino:"))
		AlterarPortaDeComunicacao(escolha)

	if(opcao2==9):
		with open('Configuracoes.json', 'w') as file:
			json.dump(ConfiguracaoPadrao, file, indent=4)
			file.close()
		
		
