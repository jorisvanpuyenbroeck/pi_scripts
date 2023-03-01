import wiringpi as wp
import time

ldr_pin = 1
button_pin = 2
led_pins = [4,6,9,10]

wp.wiringPiSetup()  # cleaning up
wp.pinMode(ldr_pin, 0)    # input
wp.pinMode(button_pin, 0)    # input

for pin in led_pins:
    wp.pinMode(pin, 1)            # Set pins to mode 1 ( OUTPUT )


def light_leds():
    for pin in led_pins:
        wp.digitalWrite(pin, 1)  # Set pins to mode 1 ( OUTPUT )

def turn_off_leds():
    for pin in led_pins:
        wp.digitalWrite(pin, 0)  # Set pins to mode 1 ( OUTPUT )

try:
    while True:
        if(wp.digitalRead(ldr_pin) == 0 
           or wp.digitalRead(button_pin) == 1): 
            print("light on")
            light_leds()
            time.sleep(0.5) #anti bouncing
        else:
            print("light off")
            turn_off_leds()
            time.sleep(0.5) #anti bouncing

except KeyboardInterrupt:
    pass
#cleanup
print("Done")