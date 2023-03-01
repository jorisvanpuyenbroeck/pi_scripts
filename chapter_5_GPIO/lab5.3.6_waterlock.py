import wiringpi as wp
import time

# Wave drive

Seq = [0, 1, 2, 3]
Seq[0] = [1, 0, 0, 0]
Seq[1] = [0, 1, 0, 0]
Seq[2] = [0, 0, 1, 0]
Seq[3] = [0, 0, 0, 1]

trig_pin = 1
echo_pin = 2
step_pins = [3, 4, 6, 9]

wp.wiringPiSetup()  # cleaning up
wp.pinMode(trig_pin, 1)     # output
wp.pinMode(echo_pin, 0)     # input

# Set all stepper motor pins as output
for pin in step_pins:
    wp.pinMode(pin, 1)
    wp.digitalWrite(pin, 0)

def measure():
    wp.digitalWrite(trig_pin, 1)
    time.sleep(0.00001)
    wp.digitalWrite(trig_pin, 0)

    while wp.digitalRead(echo_pin) == 0:
        pass
    signal_start = time.time()
    while wp.digitalRead(echo_pin) == 1:
        pass
    signal_end = time.time()

    signal_time = signal_end - signal_start
    distance = signal_time * 17000
    time.sleep(0.5)
    return distance

def open_lock():
    for i in range(0, 512):
        for step in range(0, 4):
            for pin in range(0, 4):
                xpin = step_pins[pin]  # get GPIO number
                if Seq[step][pin] != 0:  # check if pin in sequence is 1 or 0
                    wp.digitalWrite(xpin, True)  # set pin high
                else:
                    wp.digitalWrite(xpin, False)
        # Wait before moving on
            time.sleep(0.002)


try:
    while True:
        measurement = measure()
        if measurement > 30:
            print("Safe, waterlevel:", measurement)
        else:
            print("Alarm, waterlevel:", measurement)
            open_lock()

except KeyboardInterrupt:
    pass
# cleanup
print("Done")
