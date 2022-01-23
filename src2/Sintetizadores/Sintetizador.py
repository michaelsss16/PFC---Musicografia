# Possui todos os métodos de instanciação, configuração e uso dos sintetizadores presentes no projeto 

import pyttsx3
import json
with open('configuracoes.json') as file:
    config = json.load(file)


# Método de definição das configurações do sintetizador. 
def IniciarSintetizadorTTS():
	Robo = pyttsx3.init()
	voices = Robo.getProperty('voices')
	Robo.setProperty('voice', voices[config['Sintetizador']['Voz']].id) 
	return Robo

Sint = IniciarSintetizadorTTS()

def Imprimir(msg):
	if(config['Sintetizador']['SintetizadorLigado']):
		Sint.say(msg)
		Sint.runAndWait()
	print(msg)
	return ""

