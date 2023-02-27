import time
import wiringpi
import sys

## practice 1

def running(_pins):
    for _pin in _pins:
        wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
        time.sleep(0.1)
        wiringpi.digitalWrite(_pin, 0)    # Write 0 ( LOW ) to pin
        time.sleep(0.1)    

def turnoff(_pins):
    for _pin in _pins:                    # turn LED lights off when exiting
        wiringpi.digitalWrite(_pin, 0)

#SETUP
print("Start")
pins = [1,5,7,8]
switch_pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(switch_pin,0) # input
for pin in pins:
    wiringpi.pinMode(pin, 1)            # Set pins to mode 1 ( OUTPUT )

#MAIN
try:

    print(wiringpi.digitalRead(switch_pin))
    while True:
        if(wiringpi.digitalRead(switch_pin) == 1): #input is active up (pull down)
            print("running to left")
            time.sleep(0.3) #anti bouncing
            running(pins)
        else:
            print("running to right")
            time.sleep(0.3) #anti bouncing
            running(reversed(pins))
except KeyboardInterrupt:
    turnoff(pins)
    pass
#cleanup
print("Done")