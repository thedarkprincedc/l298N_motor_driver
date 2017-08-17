# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
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
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(StepPinForwardB, GPIO.OUT)
GPIO.setup(StepPinBackwardB, GPIO.OUT)
GPIO.setup(StepSpeed, GPIO.OUT)

global p

p = GPIO.PWM(37, 100)
p.start(70)

def forward(x):
    p.ChangeDutyCycle(50)
    GPIO.output(StepPinForward, GPIO.HIGH)
    print "forwarding running  motor "
    time.sleep(x)
    GPIO.output(StepPinForward, GPIO.LOW)

def reverse(x):
    GPIO.output(StepPinBackward, GPIO.HIGH)
    print "backwarding running motor"
    time.sleep(x)
    GPIO.output(StepPinBackward, GPIO.LOW)

def forwardB(x):
    GPIO.output(StepPinForwardB, GPIO.HIGH)
    print "forwarding running  motor "
    time.sleep(x)
    GPIO.output(StepPinForwardB, GPIO.LOW)

def reverseB(x):
    GPIO.output(StepPinBackwardB, GPIO.HIGH)
    print "backwarding running motor"
    time.sleep(x)
    GPIO.output(StepPinBackwardB, GPIO.LOW)

print "forward motor "
forward(5)
print "reverse motor"
reverse(5)

print "forward motor "
forwardB(5)
print "reverse motor"
reverseB(5)
print "Stopping motor"
GPIO.cleanup()