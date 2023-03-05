import time
import wiringpi
import sys


def pullUp():	# no pwm, just on/off
	wiringpi.digitalWrite(pin1, 1)
	wiringpi.digitalWrite(pin2, 0)
	
	# we don't stop here, we hold the gate open
	
def giveSlack(): # with pwm

	# Set pins as a softPWM output
	wiringpi.softPwmCreate(pin1, 0, 30)
	wiringpi.softPwmCreate(pin2, 0, 30)

	# Start PWM
	wiringpi.softPwmWrite(pin1, 0)
	wiringpi.softPwmWrite(pin2, 30)

	for i in range(30,-1,-1):      # from 100 to zero in steps of -1
		wiringpi.softPwmWrite(pin2, 30-i)
		time.sleep(wait_giveslack)

	wiringpi.softPwmWrite(pin1, 0)            # stop the white PWM output
	wiringpi.softPwmWrite(pin2, 0)            # stop the white PWM output

# SETUP
print("Start")
pin1 = 2
pin2 = 5
wait_giveslack = 0.2          # you can change this to slow down/speed up

wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1) 		# set pin2 as output
wiringpi.pinMode(pin2, 1) 		# set pin5 as output


try:
	pullUp()
	text = input("Press Enter to continue, or type 'q' to quit: ")
	if text == 'q':
		wiringpi.digitalWrite(pin1, 0)
		wiringpi.digitalWrite(pin2, 0)
		wiringpi.wiringPiSetup() # reset the pins
	else:	
		giveSlack()

except KeyboardInterrupt:
	wiringpi.wiringPiSetup() # reset the pins
	print("\nDone")