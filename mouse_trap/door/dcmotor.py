def pullUp(speed):
	wiringpi.softPwmWrite(pin2, 0)
	wiringpi.softPwmWrite(pin5, speed)

def pullDown(speed):
	wiringpi.softPwmWrite(pin2, speed)
	wiringpi.softPwmWrite(pin5, 0)

def fullStop():
	wiringpi.softPwmWrite(pin2, 0)
	wiringpi.softPwmWrite(pin5, 0)