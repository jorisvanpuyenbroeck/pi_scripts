import time
import wiringpi
import sys

## practice 1

def blink(_pin, _periode, _number):
    for i in range(0,_number):
        wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
        time.sleep(_periode)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(short)

def turnoff(_pin):
    wiringpi.digitalWrite(_pin, 0)

#SETUP
print("Start")
pin = 1
short = 0.5
long = 1.5

wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)            # Set pins to mode 1 ( OUTPUT )

#MAIN
try: 
    while True:
        blink(pin, short, 3)
        blink(pin, long, 3)
except KeyboardInterrupt:
    turnoff(pin)
    pass
#cleanup
print("Done")