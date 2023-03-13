import time
import wiringpi
import sys
from ch7_ClassLCD import LCD
from mpd import MPDClient

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

def PrintLCD(text):
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string(text)
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(0.2)
        lcd_1.clear()


# define buttons
button_pin_1 = 0
button_pin_2 = 1

# Setup wiringpi
wiringpi.wiringPiSetup()
wiringpi.pinMode(button_pin_1, 0) # input
wiringpi.pinMode(button_pin_2, 0) # input

# Setup SPI for lcd
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)

# Setup lcd
PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   15, #We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

pin_CS_lcd = 13
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

# Setup MPD

client = MPDClient()
client.connect("localhost", 6600)



#MAIN
try:
    while True:
        if(wiringpi.digitalRead(button_pin_1) == 1): #input is active high (pull down)
            print("button 1 pressed")
            time.sleep(0.2)

        if(wiringpi.digitalRead(button_pin_2) == 1): #input is active high (pull down)
            print("button 2 pressed")
            time.sleep(0.2)
        
        PrintLCD("Hello World")



except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(1)
    DeactivateLCD()
    print("\nProgram terminated")
    pass
#cleanup
print("Done")