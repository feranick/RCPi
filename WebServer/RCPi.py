#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
**********************************************************
* RCPi
* version: v2024.01.11.1
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************************
'''
#print(__doc__)
import sys, time
import RPi.GPIO as GPIO

#************************************
''' Main initialization routine '''
#************************************
def main():
    checkStatus(sys.argv[1])
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    runControls()
    
#************************************
''' RunManualControls '''
#************************************
def runControls():
    GPIO.output(26, True)
    time.sleep(1)
    GPIO.output(26, False)
    time.sleep(1)
    GPIO.cleanup()
#************************************
''' RunManualControls '''
#************************************
def checkStatus(status):
    print(status)
    #if status=='OPEN':
    #    print("Running OPEN")
    #else:
    #    print("Running CLOSE")
    time.sleep(0.5)
        
#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())
