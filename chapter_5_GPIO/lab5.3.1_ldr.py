import wiringpi as wp
import time

ldr_pin = 1

wp.wiringPiSetup()  # cleaning up
wp.pinMode(ldr_pin, 0)    # input

try:
    while True:
        if(wp.digitalRead(ldr_pin) == 0):
            print("dark")
            time.sleep(0.5) #anti bouncing
        else:
            print("light")
            time.sleep(0.5) #anti bouncing

except KeyboardInterrupt:
    pass
#cleanup
print("Done")