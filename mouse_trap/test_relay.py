import time
import wiringpi
import sys


#SETUP
print("Start")
relay_pin = 1

wiringpi.wiringPiSetup()

wiringpi.pinMode(relay_pin, 1) # output

on_off = ""

#MAIN
try:
    while True:
        on_off = input("Enter 1 or 0: ")
        if on_off == "1":
            wiringpi.digitalWrite(relay_pin, 1)
        elif on_off == "0":
            wiringpi.digitalWrite(relay_pin, 0)
        else:
            print("Invalid input")


except KeyboardInterrupt:
    pass
#cleanup
print("Done")