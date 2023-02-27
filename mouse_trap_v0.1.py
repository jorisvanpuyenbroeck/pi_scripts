import time
import wiringpi as wp

# SETUP
print("Start")

wp.wiringPiSetup()  # cleaning up in case wpS have been preactivated

switch_pin_1 = 2

wp.pinMode(switch_pin_1, 0)  # input

step_pins = [3, 4, 6, 9]

# Set all pins as output
for pin in step_pins:
    wp.pinMode(pin, wp.OUTPUT)
    wp.digitalWrite(pin, False)

# wait some time to start
time.sleep(0.5)

# Define some settings

WaitTime = 0.002

# forward

fw = [0, 1, 2, 3]
fw[0] = [1, 0, 0, 0]
fw[1] = [0, 1, 0, 0]
fw[2] = [0, 0, 1, 0]
fw[3] = [0, 0, 0, 1]

# reverse

rv = [0, 1, 2, 3]
rv[0] = [0, 0, 0, 1]
rv[1] = [0, 0, 1, 0]
rv[2] = [0, 1, 0, 0]
rv[3] = [1, 0, 0, 0]

toggle = 0

def move(seq):
    for i in range(0, 25):                   # 1/8 rotation
        print(i)
        for step in range(0, 4):
            for pin in range(0, 4):
                xpin = step_pins[pin]       # get GPIO number
                if seq[step][pin] != 0:     # check if pin in sequence is 1 or 0
                    wp.digitalWrite(xpin, True)  # set pin high
                else:
                    wp.digitalWrite(xpin, False)
            # Wait before moving on
            time.sleep(WaitTime)
            print("step")


# Start main loop
try:
    while True:

        if (wp.digitalRead(switch_pin_1) == 0):  # input is active low (pull up)
            print("button pressed ")
            if toggle == 0:
                move(rv)
                toggle = 1
            else:
                move(fw)
                toggle = 0

        else:
            print("button 1 released")

except KeyboardInterrupt:
    pass
# cleanup
print("Done")
