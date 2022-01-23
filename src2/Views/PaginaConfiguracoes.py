# Página de configurações
#Importações
import json 
from Sintetizadores.Sintetizador import *

def PaginaConfiguracoes():
	Imprimir("Página de configurações")
	opcao2 = input(Imprimir("1- Iniciar sintetizador de voz\n 9- Restaurar configurações iniciais\n 0- Retornar para a página inicial"))
	if(opcao2 == '1'):
		Imprimir("Você ainda tem que definir as configurações do sintetizador de voz")
	if(opcao2=='9'):
		configuracoes = {"Sintetizador": {"SintetizadorLigado": False, "Voz":4}}
		with open('Configuracoes.json', 'w') as file:
			json.dump(configuracoes, file, indent=4)
		
		
