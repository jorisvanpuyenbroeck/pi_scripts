import time
import wiringpi as wp
from lock.stepper import lock, unlock

# SETUP
print("Start")

wp.wiringPiSetup()  # cleaning up in case wpS have been preactivated

step_pins = [3, 4, 6, 9]

# Set all pins as output
for pin in step_pins:
    wp.pinMode(pin, wp.OUTPUT)
    wp.digitalWrite(pin, False)

# Define some settings

locked = False


# Start main loop
try:
    while True:
        text = input("Press 'l' to lock, 'o' to open, 'q' to quit: ")
        if text == 'q':
            if locked == True:
                locked = unlock()
            break
        elif text == 'l' and locked == False:
            locked = lock()
        elif text == 'o' and locked == True:
            locked = unlock()
        else:
            print("Cannot do that")
except KeyboardInterrupt:
    # before exiting we need to make sure the lock is open
    if locked == True:
        locked = unlock()
    pass
# cleanup
print("Done")
