import time
import wiringpi
import sys
from door.dcmotor import pullDown, pullUp, fullStop



# SETUP
print("Start")
pin2 = 2
pin5 = 5
release_time = 0.5
speed = 100

wiringpi.wiringPiSetup()

# Set pins as a softPWM output
wiringpi.softPwmCreate(pin2, 0, 100)
wiringpi.softPwmCreate(pin5, 0, 100)

# Start PWM


try:
	while True:
		text = input("Press 'u' to pull up, 'd' to pull down, 'q' to quit: ")
		if text == 'q':
			fullStop()
			break
		elif text == 'u':
			pullUp(speed)
			# time.sleep(pull_time) we keep pulling up until we get a 'd'
		elif text == 'd':
			fullStop()
			pullDown(speed)
			time.sleep(release_time)
			fullStop()
		else:
			print("Invalid input")

except KeyboardInterrupt:
	fullStop()
	print("\nDone")