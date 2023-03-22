import wiringpi as wp
import time
import threading

button1_pin = 7
button2_pin = 8



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
