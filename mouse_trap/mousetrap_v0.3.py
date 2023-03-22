import time
import wiringpi as wp
import sys
import threading
from door.dcmotor import pullDown, pullUp, fullStop
from lock.stepper import lock, unlock
from distance.distance_sensor import measure


# SETUP
print("Start")
echo_pin = 0
trig_pin = 1
button1_pin = 7
button2_pin = 8
dcmotor_pin1 = 2
dcmotor_pin2 = 5
speed = 100
locked = False
open = True
step_pins = [3, 4, 6, 9]

wp.wiringPiSetup()

# Set dist_sensors pins as output and input
wp.pinMode(trig_pin, 1)     # output
wp.pinMode(echo_pin, 0)     # input

# Set all stepper pins as output
for pin in step_pins:
    wp.pinMode(pin, 1) # 1 is output
    wp.digitalWrite(pin, False)

# Set pins as a softPWM output
wp.softPwmCreate(dcmotor_pin1, 0, 100)
wp.softPwmCreate(dcmotor_pin2, 0, 100)

try:
	while True:
		measurement = measure()
		if measurement > 30 and open == True:   # catch
			if locked == True:
				locked = unlock()
			fullStop()
			pullDown(speed)
			time.sleep(0.5)
			fullStop()
			locked = lock()
			measurement = measure()
			open = False
			print("Status : Closed, Distance: ", measurement)
		elif measurement <= 30 and open == False: # release
			if locked == True:
				locked = unlock()
			pullUp(speed)
			open = True
			measurement = measure()
			print("Status : Open, Distance: ", measurement)
		else:
			measurement = measure()
			print("Status : Observing, Distance: ", measurement)
			time.sleep(1)

except KeyboardInterrupt:
	fullStop()
	if locked == True:
		locked = unlock()
	pullUp(speed)
	print("\nDone")