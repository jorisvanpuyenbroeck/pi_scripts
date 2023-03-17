import time
import wiringpi as wp
import sys
from door.dcmotor import pullDown, pullUp, fullStop
from lock.stepper import lock, unlock



# SETUP
print("Start")
dcmotor_pin1 = 2
dcmotor_pin2 = 5
release_time = 0.5
speed = 100
locked = False
step_pins = [3, 4, 6, 9]

wp.wiringPiSetup()

# Set all stepper pins as output
for pin in step_pins:
    wp.pinMode(pin, 1) # 1 is output
    wp.digitalWrite(pin, False)

# Set pins as a softPWM output
wp.softPwmCreate(dcmotor_pin1, 0, 100)
wp.softPwmCreate(dcmotor_pin2, 0, 100)

# Start PWM


try:
	while True:
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