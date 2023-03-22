import time
import wiringpi as wp
import sys
import threading
from door.dcmotor import pullDown, pullUp, fullStop
from lock.stepper import lock, unlock
from distance.distance_sensor import measure
from screen.lcd import lcd

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
must_open = False
button1 = False
button2 = False
step_pins = [3, 4, 6, 9]
exit_event = threading.Event()
button1_pressed = threading.Event()
button2_pressed = threading.Event()

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

# Set button pins as input
wp.pinMode(button1_pin, 0)         # Set pin to mode 0 ( INPUT )
wp.pinMode(button2_pin, 0)  


def buttons(button1_pressed, button2_pressed, exit_event):
    while True:
        if(wp.digitalRead(button1_pin) == 1): #input is active up (pull down)
            button1_pressed.set()
            time.sleep(0.3) #anti bouncing
        if(wp.digitalRead(button2_pin) == 1): #input is active up (pull down)
            button2_pressed.set()
            time.sleep(0.3) #anti bouncing
        if exit_event.is_set():
            break

#create two new threads
t1 = threading.Thread(target=buttons, args=(button1_pressed, button2_pressed, exit_event))
t2 = threading.Thread(target=lcd)

#start the threads
t1.start()
t2.start()

try:
	while True:

		if button1_pressed.is_set():
			print("button 1 pressed")
			button1 = True
			button1_pressed.clear()
		if button2_pressed.is_set():
			print("button 2 pressed")
			button2 = True
			button2_pressed.clear()

		measurement = measure()
		
		if button2 or measurement < 30 :
			must_open = True
			button2 = False
		elif button1 or measurement >= 30 :
			must_open = False
			button1 = False
		else:
			must_open = open

		if not must_open and open:   # catch
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
		elif must_open and not open: # release
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