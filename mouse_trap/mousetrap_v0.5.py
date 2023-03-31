import time
import wiringpi as wp
import sys
import threading
import requests
from door.dcmotor import pullDown, pullUp, fullStop
from lock.stepper import lock, unlock
from distance.distance_sensor import measure
from button.button import buttons
from light.relay import light_on, light_off
from screen.lcd import ActivateLCD, DeactivateLCD
from screen.ClassLCD import LCD
from live.stream import open_stream, close_stream

# SETUP
print("Start")
echo_pin = 0
trig_pin = 1
green_pin = 8
red_pin = 7
dcmotor_pin1 = 2
dcmotor_pin2 = 5
light_pin = 15
pin_CS_lcd = 13
speed = 100
locked = False
open = True
must_open = False
green = False
red = False
light = False
stream = False
number_trapped = 0
step_pins = [3, 4, 6, 9]
url = "http://itfactory012345678.hub.ubeac.io/iotjorisvp"
uid = "iotjorisvp"
status = 0
exit_event = threading.Event()
green_pressed = threading.Event()
red_pressed = threading.Event()

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   16, 
                'CS'    :   13,
                'RST'   :   10,
                'LED'   :   12,   
}

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

# Set light pin as output
wp.pinMode(light_pin, 1)

# Set button pins as input
wp.pinMode(green_pin, 0)         # Set pin to mode 0 ( INPUT )
wp.pinMode(red_pin, 0)  

# Set SPI pins as output and activate lcd
wp.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wp.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd = LCD(PIN_OUT)

#create two new threads
t1 = threading.Thread(target=buttons, args=(green_pressed, red_pressed, exit_event))
# t2 = threading.Thread(target=beac)

#start the threads
t1.start()
# t2.start()

# main loop

# start streaming

stream = open_stream()

try:
	
	lcd.clear()
	lcd.set_backlight(0)

	while True:

		# lcd output
		current_time = time.time()
		date_string = time.strftime("%d/%m/%Y", time.localtime(current_time))
		time_string = time.strftime("%H:%M:%S", time.localtime(current_time))
		trapped_string = str(number_trapped)

		status_string = 'Armed' if open else 'Trapped'

		ActivateLCD()
		lcd.clear()
		lcd.go_to_xy(0, 0)
		lcd.put_string(date_string + '\n' + time_string + '\n' + 'Stat: ' + status_string + '\n' + 'Trapped: ' + trapped_string + '\n')
		lcd.refresh()
		DeactivateLCD()

		# ubeac output

		status = 100 if open else 0
		data= {"id": uid,"sensors":[{'id': 'status','data': status},{'id': 'number trapped','data': number_trapped}]}
		r = requests.post(url, verify=False, json=data)

		if green_pressed.is_set():
			print("Green button pressed")
			green = True
			green_pressed.clear()
		if red_pressed.is_set():
			print("Red button pressed")
			red = True
			red_pressed.clear()

		measurement = measure()
		
		if measurement >= 30 :
			print("Mouse in cage. Door must be closed")
			must_open = False
			if green:
				print("However, green button was pressed. Door must be opened")
				must_open = True
				green = False
			# ook iets doen met red

		else :
			print("No mouse in cage. Door must be opened")
			must_open = True
			if red:
				print("However, red button was pressed. Door must be closed")
				must_open = False
				red = False

		if not must_open and open:   # catch
			locked = unlock() if locked else locked
			fullStop()
			pullDown(speed)
			time.sleep(0.5)
			fullStop()
			locked = lock()
			measurement = measure()
			open = False
			light = light_on()
			number_trapped += 1
			print("Status : Closed, Distance: ", measurement)
		elif must_open and not open: # release
			locked = unlock() if locked else locked
			pullUp(speed)
			open = True
			measurement = measure()
			light = light_off()
			print("Status : Open, Distance: ", measurement)
		else:
			measurement = measure()
			print("Status : Observing, Distance: ", measurement)
			time.sleep(1)

except KeyboardInterrupt:
	print("KeyboardInterrupt")
	exit_event.set()
	lcd.clear()
	lcd.refresh()
	lcd.set_backlight(1)
	DeactivateLCD()
	fullStop()
	locked = unlock() if locked else locked
	light = light_off() if light else light
	pullUp(speed)
	fullStop()
	stream = close_stream()
	print("\nDone")