import pyfirmata
import time 
from tkinter import *

def move_servo(angle):
	pin10.write(angle)
	
def main2():
	global pin10
	
	board=pyfirmata.Arduino('COM3')

	iter8 = pyfirmata.util.Iterator(board)
	iter8.start()

	pin10 = board.get_pin('d:10:s')
	
	root = Tk()
	scale = Scale(root, command = move_servo, to = -90, 
				  orient = VERTICAL, length = 400, label = 'Angle')
	scale.pack(anchor = CENTER)

	root.mainloop()

def main():
	global pin10
	
	board=pyfirmata.Arduino('COM3')

	iter8 = pyfirmata.util.Iterator(board)
	iter8.start()

	pin10 = board.get_pin('d:10:s')
	pin10.write(110)
	time.sleep(5)
	pin10.write(20)
	exit()
	

main()