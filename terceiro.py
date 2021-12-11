from pyfirmata import ArduinoMega, util
import time                     
def Configure():
	board = ArduinoMega('COM5')
	an0 =  board.get_pin('a:0:i')
	it = util.Iterator(board)
	it.start()
	board.analog[0].enable_reporting()
	return an0

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

an0 = Configure()
EsperarBotaoSerPressionado(an0)
print("Botão acionado com sucesso!")


#valor = board.analog[0].read()
#print(valor)
