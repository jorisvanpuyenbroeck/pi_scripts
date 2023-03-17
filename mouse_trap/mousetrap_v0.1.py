import time
import wiringpi as wp
import sys
from door.dcmotor import pullDown, pullUp, fullStop
from lock.stepper import lock, unlock
from distance.distance_sensor import measure


# SETUP
print("Start")
echo_pin = 0
trig_pin = 1
dcmotor_pin1 = 2
dcmotor_pin2 = 5
release_time = 0.5
speed = 100
locked = False
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
		print("Distance: ", measurement)
		text = input("Press 'u' to pull up, 'd' to pull down, 'q' to quit: ")
		if text == 'q':
			fullStop()
			if locked == True:
				locked = unlock()
			break
		elif text == 'u':
			if locked == True:
				locked = unlock()
			pullUp(speed)
			# time.sleep(pull_time) we keep pulling up until we get a 'd'
		elif text == 'd':
			if locked == True:
				locked = unlock()
			fullStop()
			pullDown(speed)
			time.sleep(release_time)
			fullStop()
			locked = lock()
		else:
			print("Invalid input")

except KeyboardInterrupt:
	fullStop()
	print("\nDone")