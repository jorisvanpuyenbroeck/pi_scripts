import time
import wiringpi as wp

wait_time = 0.002
step_pins = [3, 4, 6, 9]

# forward

fw = [0, 1, 2, 3]
fw[0] = [1, 0, 0, 0]
fw[1] = [0, 1, 0, 0]
fw[2] = [0, 0, 1, 0]
fw[3] = [0, 0, 0, 1]

# reverse

rv = [0, 1, 2, 3]
rv[0] = [0, 0, 0, 1]
rv[1] = [0, 0, 1, 0]
rv[2] = [0, 1, 0, 0]
rv[3] = [1, 0, 0, 0]

def move(seq):
    for i in range(0, 100):                   # 100 is 1/3 rotation to open/close lock
        for step in range(0, 4):
            for pin in range(0, 4):
                xpin = step_pins[pin]       # get GPIO number
                if seq[step][pin] != 0:     # check if pin in sequence is 1 or 0
                    wp.digitalWrite(xpin, True)  # set pin high
                else:
                    wp.digitalWrite(xpin, False)
            # Wait before moving on
            time.sleep(wait_time)

def lock():
    print("Locking ")
    move(fw)
    return True

def unlock():
    print("Unlocking ")
    move(rv)
    return False