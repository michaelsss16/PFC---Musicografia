from pyfirmata import ArduinoMega, util
import time                     
board = ArduinoMega('COM5')
an0 =  board.get_pin('a:0:i')
it = util.Iterator(board)
it.start()
time.sleep(0.05)
board.analog[0].enable_reporting()
#valor = board.analog[0].read()
#print(valor)
valor = an0.read()
print(valor)
while(1):
    board.digital[15].write(1)