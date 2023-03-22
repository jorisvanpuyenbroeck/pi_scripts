import time
import wiringpi
import sys


#SETUP
print("Start")
relay_pin = 2

wiringpi.wiringPiSetup()

wiringpi.pinMode(relay_pin, 1) # output

on_off = ""

#MAIN
try:
    while True:
        on_off = input("Enter 1 or 0: ")
        if on_off == "1":
            wiringpi.digitalWrite(relay_pin, True)
        elif on_off == "0":
            wiringpi.digitalWrite(relay_pin, False)
        else:
            print("Invalid input")


except KeyboardInterrupt:
    pass
#cleanup
print("Done")