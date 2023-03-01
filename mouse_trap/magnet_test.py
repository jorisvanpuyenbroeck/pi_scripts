import time
import wiringpi

#SETUP
print("Start")
pin = 2
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin, 1)         # Set pin to mode 1 ( OUTPUT )

#MAIN
try:
    while True:
        wiringpi.digitalWrite(pin, 1)    # Write 1 ( HIGH ) to pin
        print("on", wiringpi.digitalRead(pin))
        time.sleep(5)
        wiringpi.digitalWrite(pin, 0)    # Write 1 ( low) to pin
        print("off", wiringpi.digitalRead(pin))
        time.sleep(5)
except KeyboardInterrupt:
    pass
#cleanup
print("Done")