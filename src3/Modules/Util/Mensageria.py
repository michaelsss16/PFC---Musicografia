from Modules.Sintetizador.TTS import *

Robo = IniciarSintetizadorTTS()

def Imprimir(msg):
	Robo.say(msg)
	Robo.runAndWait()
	print(msg)

