import time
import wiringpi
import sys


def pullUp(speed):
	wiringpi.softPwmWrite(pin2, 0)
	wiringpi.softPwmWrite(pin5, speed)

def pullDown(speed):
	wiringpi.softPwmWrite(pin2, speed)
	wiringpi.softPwmWrite(pin5, 0)

def fullStop():
	wiringpi.softPwmWrite(pin2, 0)
	wiringpi.softPwmWrite(pin5, 0)

# SETUP
print("Start")
pin2 = 2
pin5 = 5
pull_time = 10
pause_time = 2
speed = 100

wiringpi.wiringPiSetup()

# Set pins as a softPWM output
wiringpi.softPwmCreate(pin2, 0, 100)
wiringpi.softPwmCreate(pin5, 0, 100)

# Start PWM


try:
	while True:
		text = input("Press 'u' to pull up, 'd' to pull down, 'p' to pause, 'q' to quit: ")
		if text == 'q':
			fullStop()
			break
		elif text == 'u':
			pullUp(speed)
			time.sleep(pull_time)
			fullStop()
		elif text == 'd':
			end = time.time() + pull_time
			pullDown(speed)
			time.sleep(pull_time)
			fullStop()
		elif text == 'p':
			fullStop()
			time.sleep(pause_time)
		else:
			print("Invalid input")

except KeyboardInterrupt:
	fullStop()
	print("\nDone")