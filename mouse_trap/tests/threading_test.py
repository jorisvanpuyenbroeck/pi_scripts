import time
import threading
import wiringpi

exit_event = threading.Event()

#SETUP
print("Start")

button1_pin = 7
button2_pin = 8

wiringpi.wiringPiSetup() 
wiringpi.pinMode(button1_pin, 0)         # Set pin to mode 0 ( INPUT )
wiringpi.pinMode(button2_pin, 0)            # Set pin to mode 1 ( OUTPUT )


def buttons():
    while True:
        if(wiringpi.digitalRead(button1_pin) == 1): #input is active up (pull down)
            print("button 1 pressed")
            time.sleep(0.3) #anti bouncing
        if(wiringpi.digitalRead(button2_pin) == 1): #input is active up (pull down)
            print("button 2 pressed")
            time.sleep(0.3) #anti bouncing
        if exit_event.is_set():
            break


def lcd():
    i=0
    while True:
        i+=1
        print("lcd", i)
        time.sleep(5)
        if exit_event.is_set():
            break

#create two new threads
t1 = threading.Thread(target=buttons)
t2 = threading.Thread(target=lcd)

#start the threads
t1.start()
t2.start()

#init counter
n=0

#main function
try:
    while True:
        n+=1
        print("Main thread: ", n)
        time.sleep(1) 
except KeyboardInterrupt:
    exit_event.set()