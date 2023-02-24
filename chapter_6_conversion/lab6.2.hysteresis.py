import wiringpi
import time
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
def read_LED_state(pin_led):
    wiringpi.pinMode(pin_led, 0)                # Set led to mode 0 ( INPUT )
    state_led = wiringpi.digitalRead(pin_led)
    return state_led

def set_LED_state(pin_led, state_led):
    wiringpi.pinMode(pin_led, 1)                # Set led to mode 1 ( OUTPUT )
    wiringpi.digitalWrite(pin_led, state_led)

#Setup
pin_led_A = 1
pin_led_B = 2
state_led_A = 0
state_led_B = 0
pin_CS_adc = 16                                 #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)
hysteresis = 0.05                               # 5% hysteresis

#Main
try:
    while True:
        activate_ADC()
        tmp0 = read_ADC(0) # read channel 0
        deactivate_ADC()
        activate_ADC()
        tmp1 = read_ADC(1) # read channel 1
        deactivate_ADC()
        print ("input0:",tmp0,"input1:",tmp1)

        if abs(tmp0-tmp1) <= hysteresis*1023:           # hysteresis geval
            print("hysteresis")
            if state_led_A == 1:
                set_LED_state(pin_led_A, 1)
                set_LED_state(pin_led_B, 0)
            else:
                set_LED_state(pin_led_A, 0)
                set_LED_state(pin_led_B, 1)
        else: 
            print("no hysteresis")
            if tmp0 > tmp1:
                print("tmp0 > tmp1")
                set_LED_state(pin_led_A, 1)
                set_LED_state(pin_led_B, 0)
            else:
                print("tmp0 < tmp1")
                set_LED_state(pin_led_A, 0)
                set_LED_state(pin_led_B, 1)
        time.sleep(0.2)

        state_led_A = read_LED_state(pin_led_A)
        state_led_B = read_LED_state(pin_led_B)

except KeyboardInterrupt:
    deactivate_ADC()
    print("\nProgram terminated")