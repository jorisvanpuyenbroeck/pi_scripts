#!/usr/bin/env python
 
# import required libs
import time
import wiringpi as wp

wp.wiringPiSetup() #cleaning up in case wpS have been preactivated
 
# Use BCM wp references
# instead of physical pin numbers
 
# be sure you are setting pins accordingly
# wp10,wp9,wp11,GPI25
StepPins = [3,4,6,9]
 
# Set all pins as output
for pin in StepPins:
  wp.pinMode(pin,wp.OUTPUT)
  wp.digitalWrite(pin, False)

#wait some time to start
time.sleep(0.5)
 
# Define some settings
StepCounter = 0
WaitTime = 0.0015
 
# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = list(range(0, StepCount1))
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]
 
# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = []
Seq2 = list(range(0, StepCount2))
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

#Full torque
StepCount3 = 4
Seq3 = []
Seq3 = [3,2,1,0]
Seq3[0] = [0,0,1,1]
Seq3[1] = [1,0,0,1]
Seq3[2] = [1,1,0,0]
Seq3[3] = [0,1,1,0]
 
# set
Seq = Seq2
StepCount = StepCount2
 
# Start main loop
try:
  while 1==1:
    for pin in range(0, 4):
      xpin = StepPins[pin]
      if Seq[StepCounter][pin]!=0:
        #print " Step %i Enable %i" %(StepCounter,xpin)
        wp.digitalWrite(xpin, True)
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