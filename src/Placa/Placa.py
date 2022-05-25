from pyfirmata import Arduino, util
import time                     
from Utils.Util import *

#Tentativa de conexão com a placa arduino
try: 
	board = Arduino(Configuracoes["Arduino"]["Porta"])
except:
	escolha = input(Imprimir("Não foi possível se conectar com a placa.\n Digite 0 para finalizar o programa ou um dígito com a nova porta de comunicação."))
	if escolha == '0':
		raise Exception(Imprimir("Não foi possível se conectar com a placa. Verifique a conexão"))
	else:
		AlterarPortaDeComunicacao(escolha)
		raise Exception(Imprimir("Reinicie o programa para aplicar as modificações."))

# Definição das portas utilizadas da arduino
botaoReset =  board.get_pin('d:4:i')
botaoAvanco = board.get_pin('d:2:i')
botaoRecuo = board.get_pin('d:7:i')
ponto1 = board.get_pin('d:3:s')
ponto2 = board.get_pin('d:5:s')
ponto3 = board.get_pin('d:6:s')
ponto4 = board.get_pin('d:9:s')
ponto5 = board.get_pin('d:10:s')
ponto6= board.get_pin('d:11:s')
buzzer = board.get_pin('d:8:o')

it = util.Iterator(board)
it.start()
board.analog[1].enable_reporting()

# Funções de manipulação que envolvem a placa 
def AtivarMotores(cela):
	maxang = 0
	minAng = 90
	ponto1.write(maxang) if cela[0] else ponto1.write(minAng ) 
	ponto2.write(maxang ) if cela[1] else ponto2.write(minAng) 
	ponto3.write(maxang ) if cela[2] else ponto3.write(minAng ) 
	ponto4.write(maxang ) if cela[3] else ponto4.write(minAng ) 
	ponto5.write(maxang ) if cela[4] else ponto5.write(minAng ) 
	ponto6.write(maxang ) if cela[5] else ponto6.write(minAng ) 

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

def AvancoOuRecuoPressionado(avanco, recuo, reset):
	avancoPressionado = False
	recuoPressionado = False
	while(True):
		time.sleep(0.05)
		valAvanco = avanco.read()
		time.sleep(0.05)
		valRecuo = recuo.read()
		time.sleep(0.05)
		valReset = reset.read()

		if(valReset == True):
			if recuoPressionado:
				Pulsar(buzzer, 1, 2,0.1)
				return 0
			elif avancoPressionado:
				return 'END'
		if(valAvanco==True  and  not avancoPressionado):
			avancoPressionado = True
		if(avancoPressionado == True and valAvanco == False):
			break

		if(valRecuo==True  and  not recuoPressionado):
			recuoPressionado= True
		if(recuoPressionado== True and valRecuo== False):
			break

	if avancoPressionado:
		return 1
	if recuoPressionado:
		return -1

def Pulsar(porta, intensidade = 1, quantidadeDePulsos = 2, tempo=0.2, intensidadeMinima = 0):
	if not Configuracoes['Interface']['BipsBuzzer']: return 
	porta.write(0)
	for i in range(quantidadeDePulsos):
		porta.write(intensidade)
		time.sleep(tempo)
		porta.write(intensidadeMinima)
		time.sleep(tempo)

	porta.write(0);
