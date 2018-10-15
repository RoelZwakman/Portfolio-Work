import serial
import time
import Interface

#most of this code is based on the information available on this page: https://playground.arduino.cc/interfacing/python so check it out if shit ain't working! (installed python versions change how serial messages work)

def sendMessage():
	#the connection should also be allowed to establish in Arduino code. This is done with Serial.begin(9600); in the setup() method on the Arduino.
	ser = serial.Serial('COM3', 9600) #connects to the arduino via USB-port 3, at BAUD-rate 9600
	print("Establishing connection...")
	time.sleep(2) #sleep is necessary to establish a connection with the arduino

	ser.timeout = 0.5	#sets the timeout for serial port reading. this means that dropped bytes in the serial connection don't block up the entire stream by waiting for something
						#that will never arrive.
	
	inputvar = input("Enter a command sequence to send via serial port COM3: ")
	ser.write(b"%a" % inputvar) #prefaced with b to signify that it's a byte to the arduino. 
	print("Message sent.")

	ser.close() #close the serial connection
	print("Connection closed.")
	


