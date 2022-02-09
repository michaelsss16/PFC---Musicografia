from Views.PaginaConfiguracoes import *
from pyfirmata import ArduinoMega, util
import time                     



def Configure():
	board = ArduinoMega('COM5')
	an0 =  board.get_pin('a:0:i')
	it = util.Iterator(board)
	it.start()
	board.analog[0].enable_reporting()
	return an0

an0 = Configure()

def ReadAnalog(port):
	time.sleep(0.1)
	return an0.read()


def EsperarBotaoSerPressionado(an0):
	BotaoPresssionado = 0
	while(1):
		time.sleep(0.5)
		val = (ReadAnalog(an0))*100
		#print(val)
		if(val>=90):
			#print("Botão pressionado!")
			BotaoPresssionado=1
		if((BotaoPresssionado==1 )and (val<=90)):
			break;
	return True

def PaginaExecucao():
	Imprimir("Execução da partitura iniciada")
	with open('./PartituraInicial.txt') as file:
		texto = file.readlines()
	for linha in texto:
		for nota in linha:
			EsperarBotaoSerPressionado(an0)
			Imprimir(nota)
			Imprimir(ord(nota))
			Imprimir(bin(ord(nota)-97))
