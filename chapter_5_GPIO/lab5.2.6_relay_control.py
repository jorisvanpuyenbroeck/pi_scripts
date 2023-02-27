import time
import wiringpi
import sys


#SETUP
print("Start")
switch_pin_1 = 2
switch_pin_2 = 1
relay_pin_1 = 4
relay_pin_2 = 6

wiringpi.wiringPiSetup()
wiringpi.pinMode(switch_pin_1, 0) # input
wiringpi.pinMode(switch_pin_2, 0) # input

wiringpi.pinMode(relay_pin_1, 1) # output
wiringpi.pinMode(relay_pin_2, 1) # output


#MAIN
try:
    while True:
        wiringpi.digitalWrite(relay_pin_1, 1)
        wiringpi.digitalWrite(relay_pin_2, 1)

        if(wiringpi.digitalRead(switch_pin_1) == 0): #input is active low (pull up)
            print("activate relay 1")
            wiringpi.digitalWrite(relay_pin_1, 0)

        if(wiringpi.digitalRead(switch_pin_2) == 0): #input is active low (pull up)
            print("activate relay 2")
            wiringpi.digitalWrite(relay_pin_2, 0)

except KeyboardInterrupt:
    pass
#cleanup
print("Done")