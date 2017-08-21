

from triangula.input import SixAxis, SixAxisResource
import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()
print " mode ="+str(mode)
GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=11
StepPinBackward=15
StepPinForwardB=16
StepPinBackwardB=18
StepSpeed=37
StepSpeed2=38
sleeptime=1
_DEFAULT_TIME_=0.05

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(StepPinForwardB, GPIO.OUT)
GPIO.setup(StepPinBackwardB, GPIO.OUT)

GPIO.setup(StepSpeed, GPIO.OUT)
GPIO.setup(StepSpeed2, GPIO.OUT)

global p
global pB
p = GPIO.PWM(37, 100)
p.start(100)
pB = GPIO.PWM(38, 100)
pB.start(100)

# Button handler, will be bound to the square button later
# def handler(button):
#   print 'Button {} pressed'.format(button)
#   if button==SixAxis.BUTTON_SQUARE:
#       p.ChangeDutyCycle(buttonSquareDuty)
#       GPIO.output(StepPinForward, GPIO.HIGH)
#       time.sleep(_DEFAULT_TIME_)
#       #GPIO.output(StepPinForward, GPIO.LOW)
#   if button==SixAxis.BUTTON_CIRCLE:    
#       GPIO.output(StepPinBackward, GPIO.HIGH)
#       time.sleep(_DEFAULT_TIME_)
#       GPIO.output(StepPinBackward, GPIO.LOW)

# Get a joystick, this will fail unless the SixAxis controller is paired and active
# The bind_defaults argument specifies that we should bind actions to the SELECT and START buttons to
# centre the controller and reset the calibration respectively.

def setmotors():
    GPIO.output(StepPinForward, GPIO.HIGH)
    GPIO.output(StepPinForward, GPIO.LOW)

with SixAxisResource(bind_defaults=True) as joystick:
    # Register a button handler for the square button
    # joystick.register_button_handler(handler, SixAxis.BUTTON_SQUARE)
    # joystick.register_button_handler(handler, SixAxis.BUTTON_CIRCLE)
    while 1:
        # Read the x and y axes of the left hand stick, the right hand stick has axes 2 and 3
        x = joystick.axes[0].corrected_value()
        y = joystick.axes[1].corrected_value()

        xB = joystick.axes[2].corrected_value()
        yB = joystick.axes[3].corrected_value()

        if(y > 0.6):
            GPIO.output(StepPinForward, GPIO.HIGH)
            GPIO.output(StepPinBackward, GPIO.LOW)
            GPIO.output(StepPinForwardB, GPIO.HIGH)
            GPIO.output(StepPinBackwardB, GPIO.LOW)
        elif(y < -0.6):    
            GPIO.output(StepPinBackward, GPIO.HIGH)
            GPIO.output(StepPinForward, GPIO.LOW)
            GPIO.output(StepPinBackwardB, GPIO.HIGH)
            GPIO.output(StepPinForwardB, GPIO.LOW)
        else:
            GPIO.output(StepPinForward, GPIO.LOW)
            GPIO.output(StepPinBackward, GPIO.LOW)
            GPIO.output(StepPinForwardB, GPIO.LOW)
            GPIO.output(StepPinBackwardB, GPIO.LOW)
        if(xB > 0.6):
            p.ChangeDutyCycle(0)
            pB.ChangeDutyCycle( xB * 100)
        elif(xB < -0.6):
            p.ChangeDutyCycle(100)
            pB.ChangeDutyCycle(0)
        else:
            p.ChangeDutyCycle(100)
            pB.ChangeDutyCycle(100)
        if(yB > 0.6):
            GPIO.output(StepPinBackward, GPIO.LOW)
            GPIO.output(StepPinForward, GPIO.HIGH)
            GPIO.output(StepPinBackwardB, GPIO.HIGH)
            GPIO.output(StepPinForwardB, GPIO.LOW)
        elif(yB < -0.6):
            GPIO.output(StepPinBackward, GPIO.HIGH)
            GPIO.output(StepPinForward, GPIO.LOW)
            GPIO.output(StepPinBackwardB, GPIO.LOW)
            GPIO.output(StepPinForwardB, GPIO.HIGH)
        print(x,y)
        time.sleep(_DEFAULT_TIME_)