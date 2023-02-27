#!/usr/bin/env python

# import required libs
import time
import wiringpi as wp


#SETUP
print("Start")

wp.wiringPiSetup()  # cleaning up in case wpS have been preactivated

switch_pin_1 = 2

wp.pinMode(switch_pin_1, 0) # input

step_pins = [3, 4, 6, 9]

# Set all pins as output
for pin in step_pins:
    wp.pinMode(pin, wp.OUTPUT)
    wp.digitalWrite(pin, False)

# wait some time to start
time.sleep(0.5)

# Define some settings

WaitTime = 0.002

# Wave drive

Seq1 = [0, 1, 2, 3]
Seq1[0] = [1, 0, 0, 0]
Seq1[1] = [0, 1, 0, 0]
Seq1[2] = [0, 0, 1, 0]
Seq1[3] = [0, 0, 0, 1]

# Full step

Seq2 = [0, 1, 2, 3]
Seq2[0] = [1, 1, 0, 0]
Seq2[1] = [0, 1, 1, 0]
Seq2[2] = [0, 0, 1, 1]
Seq2[3] = [1, 0, 0, 1]

# reverse

Seq3 = [0, 1, 2, 3]
Seq3[0] = [0, 0, 0, 1]
Seq3[1] = [0, 0, 1, 0]
Seq3[2] = [0, 1, 0, 0]
Seq3[3] = [1, 0, 0, 0]

def rotate(seq):
    for step in range(0, 4):
        for pin in range(0, 4):
            xpin = step_pins[pin]  # get GPIO number
            if seq[step][pin] != 0:  # check if pin in sequence is 1 or 0
                wp.digitalWrite(xpin, True)  # set pin high
            else:
                wp.digitalWrite(xpin, False)
    # Wait before moving on
        time.sleep(WaitTime)


# Start main loop
try:
    while True:

        if(wp.digitalRead(switch_pin_1) == 0): #input is active low (pull up)
            print("button 1 pressed ")
            rotate(Seq1)
        else: 
            print("button 1 released")
            rotate(Seq3)

except KeyboardInterrupt:
    pass
#cleanup
print("Done")