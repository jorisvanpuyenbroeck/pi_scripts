import wiringpi
import time
import requests
import json


#Setup
wiringpi.wiringPiSetup() 
url = "http://itfactory012345678.hub.ubeac.io/iotjorisvp"
uid = "iotjorisvp"
status = 0
trapped = 2

#Main
try:
    while True:
        time.sleep(0.2)

        data= {
            "id": uid,
            "sensors":[{
                'id': 'status',
                'data': status
                },
                {'id': 'number trapped',
                'data': trapped
                }]
        }
     
        r = requests.post(url, verify=False, json=data)
        print(status, trapped)
        time.sleep(1)


except KeyboardInterrupt:
    print("\nProgram terminated")