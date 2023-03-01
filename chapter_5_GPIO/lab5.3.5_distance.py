import wiringpi as wp
import time

trig_pin = 1
echo_pin = 2


wp.wiringPiSetup()  # cleaning up
wp.pinMode(trig_pin, 1)     # output
wp.pinMode(echo_pin, 0)     # input


try:
    while True:
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
        dinstance = signal_time * 17000
        print("Distance: %f" % dinstance)
        time.sleep(0.5)


except KeyboardInterrupt:
    pass
#cleanup
print("Done")