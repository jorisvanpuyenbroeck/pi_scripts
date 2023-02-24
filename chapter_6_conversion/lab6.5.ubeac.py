import wiringpi
import time
import requests
import json

def activate_ADC ():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)
def deactivate_ADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)
def read_ADC(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    return adcout

#Setup
pin_CS_adc = 16                                 #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)
url = "http://itfactory012345678.hub.ubeac.io/iotjorisvp"
uid = "iotjorisvp"

#Main
try:
    while True:
        activate_ADC()
        temp = round((3.3 * read_ADC(0) * 100 ) / 1023, 2) # read channel 0, apply formula, round to 2 decimals
        deactivate_ADC()
        activate_ADC()
        light = round((read_ADC(1) * 100 ) / 1023, 2) # read channel 1, apply formula, round to 2 decimals
        deactivate_ADC()
        time.sleep(0.2)

        data= {
            "id": uid,
            "sensors":[{
                'id': 'adc ch0',
                'data': temp
                },
                {'id': 'adc ch1',
                'data': light
                }]
        }
     
        r = requests.post(url, verify=False, json=data)
        print(temp, light)
        time.sleep(1)


except KeyboardInterrupt:
    deactivate_ADC()
    print("\nProgram terminated")