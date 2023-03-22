import wiringpi as wp
import time
import threading

green_pin = 8
red_pin = 7


def buttons(green_pressed, red_pressed, exit_event):
    while True:
        if(wp.digitalRead(green_pin) == 1): #input is active up (pull down)
            green_pressed.set()
            time.sleep(0.3) #anti bouncing
        if(wp.digitalRead(red_pin) == 1): #input is active up (pull down)
            red_pressed.set()
            time.sleep(0.3) #anti bouncing
        if exit_event.is_set():
            break
