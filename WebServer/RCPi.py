#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
**********************************************************
* RCPi
* version: v2024.01.10.1
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************************
'''
#print(__doc__)
import sys, time

#************************************
''' Main initialization routine '''
#************************************
def main():
    if len(sys.argv) > 1:
        runControls(sys.argv[1])
    else:
        return

#************************************
''' RunManualControls '''
#************************************
def runControls(status):
    #print(status)
    if status=='OPEN':
        print("Running OPEN")
    else:
        print("Running CLOSE")
        
    time.sleep(0.5)
        
#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())
