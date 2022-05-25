#Importações
import json 
from Utils.Util import *
from Utils.Constantes import *

def PaginaConfiguracoes():
	Imprimir("Página de configurações")
	opcao2 = EscolherComando([0, 1, 2, 3, 8, 9], OPCOESPAGINACONFIGURACOES )
	if opcao2 == '0':
		return 
	if(opcao2 == 1):
		if Configuracoes['Sintetizador']['SintetizadorLigado']:
			Imprimir("Desativando sintetizador de voz...")
			Configuracoes['Sintetizador']['SintetizadorLigado'] =False 
			with open('Configuracoes.json', 'w') as file:
				json.dump(Configuracoes, file, indent=4)
		else:
			Imprimir("Ativando sintetizador de voz...")
			Configuracoes['Sintetizador']['SintetizadorLigado'] =True
			with open('Configuracoes.json', 'w') as file:
				json.dump(Configuracoes, file, indent=4)

	if opcao2 == 2:
		if Configuracoes['Interface']['BipsBuzzer']:
			Imprimir("Desligando bips...")
			Configuracoes['Interface']['BipsBuzzer'] =False 
			with open('Configuracoes.json', 'w') as file:
				json.dump(Configuracoes, file, indent=4)
		else:
			Imprimir("Ativando bips...")
			Configuracoes['Interface']['BipsBuzzer'] =True
			with open('Configuracoes.json', 'w') as file:
				json.dump(Configuracoes, file, indent=4)

	if opcao2 ==  3:
		AlterarVozDoSintetizador()

	if opcao2 == 8:
		escolha = input(Imprimir("Digite o número da porta que deseja atribuir para comunicação com a placa arduino:"))
		AlterarPortaDeComunicacao(escolha)

	if(opcao2==9):
		with open('Configuracoes.json', 'w') as file:
			json.dump(ConfiguracaoPadrao, file, indent=4)
			file.close()
		
		
