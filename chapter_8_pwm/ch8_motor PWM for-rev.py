import time
import wiringpi
import sys


def pullUp(sig1, wait):
	for i in range(0, 101):      	# gradually increase spead
		wiringpi.softPwmWrite(sig1, i)
		time.sleep(wait)
	print("max speed started")
	# for t in range(0, 500): 			# hold at max speed
	# 	wiringpi.softPwmWrite(sig1, 100)
	# 	time.sleep(wait)
	print("max speed ended")


def pullDown(sig2, wait):
	for i in range(100,-1,-1):      # from 100 to zero in steps of -1
		wiringpi.softPwmWrite(sig2, 100-i)
		time.sleep(wait)

# SETUP
print("Start")
pin2 = 2
pin5 = 5
pause_time = 0.02           # you can change this to slow down/speed up
wiringpi.wiringPiSetup()

# Set pins as a softPWM output
wiringpi.softPwmCreate(pin2, 0, 100)
wiringpi.softPwmCreate(pin5, 0, 100)

# Start PWM
wiringpi.softPwmWrite(pin2, 0)
wiringpi.softPwmWrite(pin5, 100)

try:
	while True:
		pullUp(pin2, pause_time)
		text = input("Press Enter to continue, or type 'q' to quit: ")
		if text == 'q':
			wiringpi.softPwmWrite(pin2, 0)            # stop the white PWM output
			wiringpi.softPwmWrite(pin5, 0)            # stop the white PWM output
			break
		pullDown(pin5,pause_time)

except KeyboardInterrupt:
	wiringpi.softPwmWrite(pin2, 0)            # stop the white PWM output
	wiringpi.softPwmWrite(pin5, 0)            # stop the white PWM output
	print("\nDone")