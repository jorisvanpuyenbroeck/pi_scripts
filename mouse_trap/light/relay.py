import wiringpi as wp

light_pin = 15

def light_on():
    print("Light on")
    wp.digitalWrite(light_pin, True)
    return True

def light_off():
    print("Light off")
    wp.digitalWrite(light_pin, False)
    return False