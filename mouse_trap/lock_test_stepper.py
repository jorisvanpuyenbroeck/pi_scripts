import time
import wiringpi as wp
from config.stepper_conf import fw, rv

# SETUP
print("Start")

wp.wiringPiSetup()  # cleaning up in case wpS have been preactivated

switch_pin_1 = 2
step_pins = [3, 4, 6, 9]

# Set all pins as output
for pin in step_pins:
    wp.pinMode(pin, wp.OUTPUT)
    wp.digitalWrite(pin, False)

# wait some time to start
time.sleep(0.5)

# Define some settings

WaitTime = 0.002
Locked = False


def move(seq):
    for i in range(0, 100):                   # 100 is 1/3 rotation to open/close lock
        for step in range(0, 4):
            for pin in range(0, 4):
                xpin = step_pins[pin]       # get GPIO number
                if seq[step][pin] != 0:     # check if pin in sequence is 1 or 0
                    wp.digitalWrite(xpin, True)  # set pin high
                else:
                    wp.digitalWrite(xpin, False)
            # Wait before moving on
            time.sleep(WaitTime)


# Start main loop
try:
    while True:
        text = input("Press 'l' to lock, 'o' to open, 'q' to quit: ")
        if text == 'q':
            if Locked == True:
                print("opening ")
                move(rv)
                Locked = False
            break
        elif text == 'l' and Locked == False:
            print("locking ")
            move(fw)
            Locked = True
        elif text == 'o' and Locked == True:
            print("opening ")
            move(rv)
            Locked = False
        else:
            print("Cannot do that")
except KeyboardInterrupt:
    # before exiting we need to make sure the lock is open
    if Locked == True:
        print("opening ")
        move(rv)
        Locked = False
    pass
# cleanup
print("Done")
