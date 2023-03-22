import pyA20.gpio as GPIO
from time import sleep

servo_pin = GPIO.PA21    # GPIO pin connected to LED
GPIO.init()    # initialize GPIO
GPIO.setcfg(servo_pin, GPIO.OUTPUT)    # set LED pin as output

pwm = GPIO.PWM(servo_pin, 100)    # create PWM instance with frequency
pwm.start(0)    # start PWM with duty cycle 0

while True:
    for duty in range(0, 101):
        pwm.set_duty_cycle(duty)    # set duty cycle
        pwm.start(1)    # start PWM
        sleep(0.01)
    sleep(0.5)
    for duty in range(100, -1, -1):
        pwm.set_duty_cycle(duty)
        pwm.start(1)
        sleep(0.01)
    sleep(0.5)