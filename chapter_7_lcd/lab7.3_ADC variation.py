
import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD


def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

def ActivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)

def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)


def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    return adcout

def stars(value):
    stars = ""
    number = int(value/102.4) + 1 # 102.4 = 1024/10
    for i in range(0, number):
        stars = stars + "*"
    return stars

# general setup
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
#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 13
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)


# Setup ADC

pin_CS_adc = 16
wiringpi.pinMode(pin_CS_adc , 1)            # Set pin to mode 1 ( OUTPUT )


try:
    lcd_1.clear()
    lcd_1.set_backlight(0)
    while True:

        ActivateADC()
        adc_value0 = readadc(0) # read adc value on channel 0
        DeactivateADC()

        print("ADC value on display in0=" + str(adc_value0))

        stars_string = stars(adc_value0)

        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string('ADC value \non display \nin0=' + stars_string)
        lcd_1.refresh()
        DeactivateLCD()

        time.sleep(1)
except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(1)
    DeactivateLCD()
    print("\nProgram terminated")