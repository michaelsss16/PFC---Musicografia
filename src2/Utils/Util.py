# Contém todos os métodos auxiliares para as principais páginas do programa

import pyttsx3
import json
#Variáveis globais
TamanhoDoVetorDeVozes = 0

# Dicionário de configuração padrão 
ConfiguracaoPadrao = {
	"Interface":
	{
		"BipsBuzzer" : True
	},
	"Sintetizador": {
		"SintetizadorLigado": False,
		"Voz": 4
	},
	"Arduino" : {
		"Porta": "COM3",
		"BotaoAvanco" : "a:0:i",
		"BotaoRecuo" : ""
	}
}

# Instanciação do objeto de configuração armazenado em arquivo 
try: 
	with open('configuracoes.json', encoding='utf-8', mode='r') as file:
		Configuracoes = json.load(file)
		file.close()
except: 
	with open('Configuracoes.json', 'w') as file:
		json.dump(ConfiguracaoPadrao, file, indent=4)
		Configuracoes = ConfiguracaoPadrao
		file.close()

# Método de tratamento das escolhas oferecidas em cada uma das páginas 
def EscolherComando(listaDeValoresPermitidos = [0], listaDeDescricoes = ['0- Finalizar\n'], mensagemDeErro = "O valor inserido não é válido. Escolha outra opção."):
	erro = False
	while not erro:
		if(len(listaDeValoresPermitidos) != len(listaDeDescricoes)):
			raise Exception ("Tamanho da lista de valores permitidos e de descrições não é compatível")
		for item in listaDeDescricoes:
			Imprimir(item)
		valorInserido = int(input(Imprimir("Digite a sua escolha:")))
		if valorInserido in listaDeValoresPermitidos:
			return valorInserido
		else:
			Imprimir(mensagemDeErro)

# Método de definição das configurações do sintetizador. 
def IniciarSintetizadorTTS():
	global TamanhoDoVetorDeVozes
	try: 
		Robo = pyttsx3.init()
		voices = Robo.getProperty('voices')
		TamanhoDoVetorDeVozes = len(voices )
		Robo.setProperty('voice', voices[Configuracoes['Sintetizador']['Voz']].id) 
		return Robo
	except:
		print("Não foi possível iniciar o sintetizador. Verifique as configurações escolhidas.")
		Configuracoes['Sintetizador']['SintetizadorLigado'] = False


Sint = IniciarSintetizadorTTS()

def Imprimir(msg):
	try:
		if(Configuracoes['Sintetizador']['SintetizadorLigado']):
			Sint.say(msg)
			Sint.runAndWait()
	except:
		print("Não foi possível iniciar o sintetizador. Verifique as configurações.")
		Configuracoes['Sintetizador']['SintetizadorLigado'] = False
	print(msg)
	return ""

# Método de controle da porta utilizada para comunicação com arduino
def AlterarPortaDeComunicacao(valorPorta):
	Configuracoes['Arduino']['Porta'] ="COM"+valorPorta
	with open('Configuracoes.json', 'w') as file:
		json.dump(Configuracoes, file, indent=4)
		file.close()

def AlterarVozDoSintetizador():
	escolha = int(input(Imprimir("Digite o número da voz desejada. Valores de 0 até  "+ str(TamanhoDoVetorDeVozes))))
	if escolha > TamanhoDoVetorDeVozes:
		Imprimir("O valor inserido não é válido.")
		return""
	Configuracoes['Sintetizador']['Voz'] =  escolha
	with open('Configuracoes.json', 'w') as file:
		json.dump(Configuracoes, file, indent=4)
		file.close()
	Sint = IniciarSintetizadorTTS()
