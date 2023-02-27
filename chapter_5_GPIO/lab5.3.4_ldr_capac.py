import wiringpi as wp
import time

ldr_pin = 1

wp.wiringPiSetup()          # cleaning up

try:
    while True:
        wp.pinMode(ldr_pin, 1)          # output
        wp.digitalWrite(ldr_pin, 0)     # turn off 
        time.sleep(0.1)

        wp.pinMode(ldr_pin, 0)          # input
        start = time.time()
        while wp.digitalRead(ldr_pin) == 0:
            pass # wait for the pin to go high
        stop = time.time()
        interval = stop - start
        print("Interval: %f" % interval)
            
except KeyboardInterrupt:
    pass
#cleanup
print("Done")