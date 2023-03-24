import wiringpi as wp
import time

pin_CS_lcd = 13

def ActivateLCD():
    wp.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)
def DeactivateLCD():
    wp.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

def display(lcd, exit_event):

    lcd.clear()
    lcd.set_backlight(0)

    
    while True:
        current_time = time.time()
        date_string = time.strftime("%d/%m/%Y", time.localtime(current_time))
        time_string = time.strftime("%H:%M:%S", time.localtime(current_time))
        ActivateLCD()
        lcd.clear()
        lcd.go_to_xy(0, 0)
        lcd.put_string(date_string +'\n'+ time_string + '\n'+ 'in0=' + str(8) + '\nin1=' + str(10))
        lcd.refresh()
        DeactivateLCD()
        time.sleep(1)
        if exit_event.is_set():
            break

