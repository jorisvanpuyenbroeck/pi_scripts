
import time
import wiringpi
import spidev
from ClassLCD import LCD

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)
def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   16, 
                'CS'    :   13,
                'RST'   :   10,
                'LED'   :   12,   
}

pin_CS_lcd = 13
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd = LCD(PIN_OUT)
current_time = time.time()
date_string = time.strftime("%d/%m/%Y", time.localtime(current_time))
time_string = time.strftime("%H:%M:%S", time.localtime(current_time))

try:
    lcd.clear()
    lcd.set_backlight(0)
    while True:
        current_time = time.time()
        date_string = time.strftime("%d/%m/%Y", time.localtime(current_time))
        time_string = time.strftime("%H:%M:%S", time.localtime(current_time))
        print (date_string)
        print (time_string)
        ActivateLCD()
        lcd.clear()
        lcd.go_to_xy(0, 0)
        lcd.put_string(date_string +'\n'+ time_string + '\n'+ 'in0=' + str(8) + '\nin1=' + str(10))
        lcd.refresh()
        DeactivateLCD()
        time.sleep(1)
except KeyboardInterrupt:
    lcd.clear()
    lcd.refresh()
    lcd.set_backlight(1)
    DeactivateLCD()
    print("\nProgram terminated")