import time
import wiringpi
import sys



#SETUP
print("Start")

button1_pin = 7
button2_pin = 8

wiringpi.wiringPiSetup() 
wiringpi.pinMode(button1_pin, 0)         # Set pin to mode 0 ( INPUT )
wiringpi.pinMode(button2_pin, 0)            # Set pin to mode 1 ( OUTPUT )

#MAIN
try: 
    while True:
        if(wiringpi.digitalRead(button1_pin) == 1): #input is active up (pull down)
            print("button 1 pressed")
            time.sleep(0.3) #anti bouncing
        if(wiringpi.digitalRead(button2_pin) == 1): #input is active up (pull down)
            print("button 2 pressed")
            time.sleep(0.3) #anti bouncing
except KeyboardInterrupt:
    pass
#cleanup
wiringpi.wiringPiSetup() 
print("Done")