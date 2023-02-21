import time
import wiringpi
import sys

## practice 1

def blink(_pins):
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
pins = [1,2,5,7]
wiringpi.wiringPiSetup()
for pin in pins:
    wiringpi.pinMode(pin, 1)            # Set pins to mode 1 ( OUTPUT )

#MAIN
try: 
    while True:
        blink(pins)
except KeyboardInterrupt:
    turnoff(pins)
    pass
#cleanup
print("Done")