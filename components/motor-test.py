# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

def motorTest():
    # Use BCM GPIO references
    # instead of physical pin numbers
    #GPIO.setmode(GPIO.BCM)
    mode=GPIO.getmode()
    print " mode ="+str(mode)
    GPIO.cleanup()

    # Define GPIO signals to use
    # Physical pins 11,15,16,18
    # GPIO17,GPIO22,GPIO23,GPIO24

    MotorA_StepPinForward=11
    MotorA_StepPinBackward=15
    MotorA_StepSpeed=37

    MotorB_StepPinForward=16
    MotorB_StepPinBackward=18
    MotorB_StepSpeed=37

    _SLEEPTIME_=5

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(MotorA_StepPinForward, GPIO.OUT)
    GPIO.setup(MotorA_StepPinBackward, GPIO.OUT)
    GPIO.setup(MotorA_StepSpeed, GPIO.OUT)

    GPIO.setup(MotorB_StepPinForward, GPIO.OUT)
    GPIO.setup(MotorB_StepPinBackward, GPIO.OUT)
    GPIO.setup(MotorB_StepSpeed, GPIO.OUT)

    # Pulse Width Modulation for Speed Control
    pWM_A = GPIO.PWM(MotorA_StepSpeed, 100)
    pWM_A.start(70)

    pWM_B = GPIO.PWM(MotorB_StepSpeed, 100)
    pWM_B.start(70)

    #Motor A
    def testMotorForwardA(x):
        GPIO.output(MotorA_StepPinForward, GPIO.HIGH)
        print "forwarding running motor A"
        time.sleep(x)
        GPIO.output(MotorA_StepPinForward, GPIO.LOW)
    def testMotorBackwardA(x):
        GPIO.output(MotorA_StepPinBackward, GPIO.HIGH)
        print "backwarding running motor A"
        time.sleep(x)
        GPIO.output(MotorA_StepPinBackward, GPIO.LOW)
    
    #Motor B
    def testMotorForwardB(x):
        GPIO.output(MotorB_StepPinForward, GPIO.HIGH)
        print "forwarding running  motor B"
        time.sleep(x)
        GPIO.output(MotorB_StepPinForward, GPIO.LOW)
    def testMotorBackwardB(x):
        GPIO.output(MotorB_StepPinBackward, GPIO.HIGH)
        print "backwarding running motor B"
        time.sleep(x)
        GPIO.output(MotorB_StepPinBackward, GPIO.LOW)

    #Both
    def testBothMotorsForward(x):
        GPIO.output(MotorA_StepPinForward, GPIO.HIGH)
        GPIO.output(MotorB_StepPinForward, GPIO.HIGH)
        print "forwarding running  motor A & B"
        time.sleep(x)
        GPIO.output(MotorA_StepPinForward, GPIO.LOW)
        GPIO.output(MotorB_StepPinForward, GPIO.LOW)

    def testBothMotorsBackward(x):
        GPIO.output(MotorA_StepPinBackward, GPIO.HIGH)
        GPIO.output(MotorB_StepPinBackward, GPIO.HIGH)
        print "backwarding running motor A & B"
        time.sleep(x)
        GPIO.output(MotorA_StepPinBackward, GPIO.LOW)
        GPIO.output(MotorB_StepPinBackward, GPIO.LOW)

    #Opposites
    def testBothOppositesMotorsA(x):
        GPIO.output(MotorA_StepPinBackward, GPIO.HIGH)
        GPIO.output(MotorB_StepPinForward, GPIO.HIGH)
        print "backwarding running motor A\nForward running motor B"
        time.sleep(x)
        GPIO.output(MotorA_StepPinBackward, GPIO.LOW)
        GPIO.output(MotorB_StepPinForward, GPIO.LOW)

    #Opposites
    def testBothOppositesMotorsB(x):
        GPIO.output(MotorA_StepPinForward, GPIO.HIGH)
        GPIO.output(MotorB_StepPinBackward, GPIO.HIGH)
        print "forward running motor A\nBackward running motor B"
        time.sleep(x)
        GPIO.output(MotorA_StepPinForward, GPIO.LOW)
        GPIO.output(MotorB_StepPinBackward, GPIO.LOW)

    testMotorForwardA(_SLEEPTIME_)
    testMotorBackwardA(_SLEEPTIME_)
    testMotorForwardB(_SLEEPTIME_)
    testMotorBackwardB(_SLEEPTIME_)
    testBothMotorsForward(_SLEEPTIME_)
    testBothMotorsBackward(_SLEEPTIME_)
    testBothOppositesMotorsA(_SLEEPTIME_)
    testBothOppositesMotorsB(_SLEEPTIME_)