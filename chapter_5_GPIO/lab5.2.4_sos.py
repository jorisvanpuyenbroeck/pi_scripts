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
led_pin = 1
switch_pin = 2
short = 0.5
long = 1.5

wiringpi.wiringPiSetup()
wiringpi.pinMode(led_pin, 1)            # Set pins to mode 1 ( OUTPUT )
wiringpi.pinMode(switch_pin, 0)            # Set pins to mode 0 ( INPUT )


#MAIN
try: 
    while True:
        if(wiringpi.digitalRead(switch_pin) == 1): #input is active up (pull down)
            print("LED not flashing")
            time.sleep(0.3) #anti bouncing
            wiringpi.digitalWrite(led_pin, 0)    # Write 0 ( LOW ) to LED
        else:
            blink(led_pin, short, 3)
            blink(led_pin, long, 3) 
except KeyboardInterrupt:
    turnoff(led_pin)
    pass
#cleanup
print("Done")