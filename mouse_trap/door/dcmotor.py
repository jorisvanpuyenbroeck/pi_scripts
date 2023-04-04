import wiringpi as wp

dcmotor_pin1 = 2
dcmotor_pin2 = 5

def pullUp(speed):
	print("Pull Up")
	wp.softPwmWrite(dcmotor_pin1, 0)
	wp.softPwmWrite(dcmotor_pin2, speed)

def pullDown(speed):
	print("Pull Down")
	wp.softPwmWrite(dcmotor_pin1, speed)
	wp.softPwmWrite(dcmotor_pin2, 0)

def fullStop():
	wp.softPwmWrite(dcmotor_pin1, 0)
	wp.softPwmWrite(dcmotor_pin2, 0)