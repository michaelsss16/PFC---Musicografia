from pyfirmata import Arduino, util
import time                     

# Definição da placa e das portas disponíveis para uso 
board = Arduino('COM3')
botaoReset =  board.get_pin('a:1:i')
botaoAvanco = board.get_pin('d:2:i')
botaoRecuo = board.get_pin('d:4:i')
buzzer = board.get_pin('d:10:p')

it = util.Iterator(board)
it.start()
board.analog[1].enable_reporting()

# Funções de manipulação que envolvem a placa 
def ReadAnalog(port):
	time.sleep(0.05)
	return port.read()

def EsperarBotaoSerPressionado(botao):
	BotaoPresssionado = 0
	while(1):
		time.sleep(0.5)
		val = (ReadAnalog(botao))*100
		#print(val)
		if(val>=90):
			#print("Botão pressionado!")
			BotaoPresssionado=1
		if((BotaoPresssionado==1 )and (val<=90)):
			break;
	return True

def AvancoOuRecuoPressionado(avanco, recuo):
	avancoPressionado = False
	recuoPressionado = False
	while(True):
		time.sleep(0.05)
		valAvanco = avanco.read()
		if(valAvanco==True  and  not avancoPressionado):
			avancoPressionado = True
			print("Pressionado")
		if(avancoPressionado == True and valAvanco == False):
			break
	print("solto")
	return True

def Pulsar(porta, intensidade = 1, quantidadeDePulsos = 2, tempo=0.2, intensidadeMinima = 0):
	# Adicionar verificação de configuração verificand se o campo interface.BipsBuzzer está ligado 
	porta.write(0)
	for i in range(quantidadeDePulsos):
		porta.write(intensidade)
		time.sleep(tempo)
		porta.write(intensidadeMinima)
		time.sleep(tempo)

	porta.write(0);
