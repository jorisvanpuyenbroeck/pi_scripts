import time
import wiringpi
import sys

## practice 1

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.5)
    wiringpi.digitalWrite(_pin, 0)    # Write 0 ( HIGH ) to pin
    time.sleep(0.5)


#SETUP
print("Start")
led_pin = 1
switch_pin = 2
relay_pin = 8

wiringpi.wiringPiSetup() 
wiringpi.pinMode(switch_pin, 0)         # Set pin to mode 0 ( INPUT )
wiringpi.pinMode(led_pin, 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(relay_pin, 1)            # Set pin to mode 1 ( OUTPUT )

#MAIN
try: 
    while True:
        if(wiringpi.digitalRead(switch_pin) == 0): #input is active low (pull up)
            print("LED flashing")
            time.sleep(0.3) #anti bouncing
            blink(led_pin)
            blink(relay_pin)
        else:
            print("LED not flashing")
            time.sleep(0.3) #anti bouncing
            wiringpi.digitalWrite(led_pin, 0)    # Write 0 ( LOW ) to LED


except KeyboardInterrupt:
    pass
#cleanup
wiringpi.wiringPiSetup() 
print("Done")