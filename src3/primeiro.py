from pyfirmata import ArduinoMega, util
import time
                                
Uno = ArduinoMega('COM5')
i = 0
                                     
print('Olá Mundo!')                  
print(str(Uno.get_firmata_version()))
                                
while (i<=5):
    i = i+1
    #Uno.iterate()
    print(str(Uno.digital[22].read()         ))
    Uno.analog[1].write(1)         
    print('LED ligado')              
    time.sleep(1)

    Uno.analog[1].write(0)         
    print('LED desligado')           
    time.sleep(1)                    

                                
Uno.exit()