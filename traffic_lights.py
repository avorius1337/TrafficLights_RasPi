#traffic_lights.py
import time
import RPi.GPIO as GPIO

#initial setup (tells the GPIO pins to set to Broadcom mode, sets GPIO pins 2, 3 and 4 as output pins)

#GPIO.setwarnings(False) just makes the shell not spit out warning errors about the pins already being assigned,
#which can be useful for testing purposes.

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setwarnings(False)

#sets all LEDs to off at the beginning of the code running
GPIO.output(2, False)
GPIO.output(3, False)
GPIO.output(4, False)

#this does the cycle of each LED 
time.sleep(1)
GPIO.output(2, True)
GPIO.output(3, False)
GPIO.output(4, False)

time.sleep(3)
GPIO.output(2, False)
GPIO.output(3, True)
GPIO.output(4, False)

time.sleep(3)
GPIO.output(2, False)
GPIO.output(3, False)
GPIO.output(4, True)

#this resets all LEDs to original state
time.sleep(3)
GPIO.output(2, True)
GPIO.output(3, True)
GPIO.output(4, True)

time.sleep(0.5)
GPIO.output(2, False)
GPIO.output(3, False)
GPIO.output(4, False)

