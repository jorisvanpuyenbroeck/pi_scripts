#!/usr/bin/env python
 
# import required libs
import time
import wiringpi as wp

wp.wiringPiSetup() #cleaning up in case wpS have been preactivated
 
# Use BCM wp references
# instead of physical pin numbers
 
# be sure you are setting pins accordingly
# wp3,wp4,wp6,wp9
StepPins = [3,4,6,9]
 
# Set all pins as output
for pin in StepPins:
  wp.pinMode(pin,wp.OUTPUT)
  wp.digitalWrite(pin, False)

#wait some time to start
time.sleep(0.5)
 
# Define some settings
StepCounter = 0
WaitTime = 0.002
 
#Wave drive
StepCount1 = 4
Seq1 = [0,1,2,3]
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]

#Full step
StepCount2 = 4
Seq2 = [0,1,2,3]
Seq2[0] = [1,1,0,0]
Seq2[1] = [0,1,1,0]
Seq2[2] = [0,0,1,1]
Seq2[3] = [1,0,0,1]

# set
Seq = Seq2   ## full step
StepCount = StepCount2
 
# Start main loop
try:
  while True:
    for pin in range(0, 4):
      xpin = StepPins[pin] ## get GPIO number
      if Seq[StepCounter][pin]!=0: ## check if pin in sequence is 1 or 0
        print (" Step %i Enable %i" %(StepCounter,xpin)) 
        wp.digitalWrite(xpin, True) ## set pin high
      else:
        wp.digitalWrite(xpin, False)
    StepCounter += 1

  # If we reach the end of the sequence
  # start again
    if (StepCounter==StepCount):
      StepCounter = 0
    if (StepCounter<0):
      StepCounter = StepCount
 
  # Wait before moving on
    time.sleep(WaitTime)
except:
    wp.wiringPiSetup() #cleaning up in case wpS have been preactivated
finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
    wp.wiringPiSetup() #cleaning up in case wpS have been preactivated
    for pin in StepPins:
      wp.pinMode(pin,wp.OUTPUT)
      wp.digitalWrite(pin, False)