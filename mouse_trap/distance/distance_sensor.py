
import time
import wiringpi as wp

echo_pin = 0
trig_pin = 1

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
