import wiringpi as wp
import time
import threading


exit_event = threading.Event()

def lcd():
    i=0
    while True:
        i+=1
        print("lcd", i)
        time.sleep(5)
        if exit_event.is_set():
            break
