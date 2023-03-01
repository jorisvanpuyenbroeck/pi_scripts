import time
import wiringpi as wp

# SETUP
print("Start")

wp.wiringPiSetup()  # cleaning up in case wpS have been preactivated

servo_pin = 2  # hardware pwm pin should be wpi2 pin, GPIO118, physical 7

wp.softPwmCreate(servo_pin, 0, 100) # soft pwm pin, initial value, range could be any pin
# wp.pinMode(servo_pin, wp.GPIO.PWM_OUTPUT)  # hardware mode pwm pin
wp.pwmSetMode(wp.GPIO.PWM_MODE_MS)   # set PWM mode
wp.pwmSetRange(100)   # set PWM range to 100 (0-100% duty cycle)
wp.pwmSetClock(500)   # set PWM clock to 500Hz


# Start main loop
try:

    while True:

        for duty in range(0, 101):
            wp.pwmWrite(servo_pin, duty)   # set duty cycle
            time.sleep(0.01)
        time.sleep(0.5)
        for duty in range(100, -1, -1):
            wp.pwmWrite(servo_pin, duty)
            time.sleep(0.01)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
# cleanup
print("Done")