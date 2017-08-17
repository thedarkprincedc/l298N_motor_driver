# Import required libraries
import sys
import time
#import RPi.GPIO as GPIO

def keyboardListener():
    print "Listening for Keyboard Input"

def testMotorListener():
    print "Testing L298N Motor Controller"

print "\nSelect a control scheme?\n \
    \n\t1. Keyboard \
    \n\t2. Gamepad (disabled) \
    \n\t3. Autonomous (disabled) \
    \n\t4. Test Motors \
    \n\t5. Web Server (disabled) \n"

menuSelection = 0

while (menuSelection <> "q"):
    menuSelection = input("=")
    if menuSelection == 1:
        keyboardListener()
        break
    elif menuSelection == 2:
        print "Selected Gamepad"
        break
    elif menuSelection == 3:
        print "Selected Autonomoua (disabled)"
        break
    elif menuSelection == 4:
        testMotorListener()
        break
    elif menuSelection == 5:
        print "Selected Web Server (disabled)"
        break
    elif menuSelection == "q":
        print "Quiting Application"
        break

