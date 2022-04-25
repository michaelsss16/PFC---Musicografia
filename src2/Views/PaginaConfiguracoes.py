#Importações
import json 
from Utils.Util import *

def PaginaConfiguracoes():
	Imprimir("Página de configurações")
	opcao2 = EscolherComando([0, 1, 2, 9], [
		'1- Iniciar/Desligar sintetizador de voz.',
		'2- Ligar/Desligarbips entre telas',
		'9- Retornar aos padrões de configuração.',
		'0- Retornar a página anterior.'
	])
	
	if(opcao2 == '1'):
		Imprimir("Você ainda tem que definir as configurações do sintetizador de voz")
	if(opcao2=='9'):
		configuracoes = {"Sintetizador": {"SintetizadorLigado": False, "Voz":4}}
		with open('Configuracoes.json', 'w') as file:
			json.dump(configuracoes, file, indent=4)
		
		
