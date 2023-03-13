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

# Setup MPD and connect

client = MPDClient()

try:
    client.connect("localhost", 6600)
except ConnectionError:
    sys.exit("Connection to MPD failed")

# radio stations

stations = [
"http://icecast.vrtcdn.be/radio1-high.mp3",
"http://icecast.vrtcdn.be/ra2ant-high.mp3",
"http://icecast.vrtcdn.be/klara-high.mp3",
"http://icecast.vrtcdn.be/stubru-high.mp3",
"http://icecast.vrtcdn.be/mnm-high.mp3" ]

# rest playlist and add stations
client.clear()
for i in range(len(stations)):
    client.add(stations[i])


#MAIN
try:
    client.play()
    current_station = client.currentsong()
    while True:
        if(wiringpi.digitalRead(button_pin_1) == 1): #input is active high (pull down)
            client.next()
            current_station = str(client.currentsong().get('name'))
            print("Next channel : " + current_station)
            PrintLCD(current_station)
            time.sleep(0.2)

        if(wiringpi.digitalRead(button_pin_2) == 1): #input is active high (pull down)
            client.previous()
            current_station = str(client.currentsong().get('name'))
            print("Previous channel : " + current_station)
            PrintLCD(current_station)
            time.sleep(0.2)


except KeyboardInterrupt:
    client.stop()
    client.disconnect()
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(1)
    DeactivateLCD()
    print("\nProgram terminated")
    pass
#cleanup
print("Done")