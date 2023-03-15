import time
import wiringpi 
import sys

def controlMotor(sig1, sig2, cnt, wait):
	wiringpi.softPwmWrite(sig1, cnt)
	wiringpi.softPwmWrite(sig2, 100-cnt)
	time.sleep(wait)


#SETUP
print("Start")
pin2 = 2
pin5 = 5
buffer_time = 0.02           # you can change this to slow down/speed up
wiringpi.wiringPiSetup() 

# Set pins as a softPWM output
wiringpi.softPwmCreate(pin2, 0, 100)
wiringpi.softPwmCreate(pin5, 0, 100)

# Start PWM
wiringpi.softPwmWrite(pin2, 0)
wiringpi.softPwmWrite(pin5, 100)

try:
	while True:
		for i in range(0,101):      	# 101 because it stops when it finishes 100
			controlMotor(pin2,pin5,i,buffer_time)
		for i in range(100,-1,-1):      # from 100 to zero in steps of -1
			controlMotor(pin2,pin5,i,buffer_time)

except KeyboardInterrupt:
	wiringpi.softPwmWrite(pin2, 0)            # stop the white PWM output
	wiringpi.softPwmWrite(pin5, 0)            # stop the white PWM output
	print("\nDone")