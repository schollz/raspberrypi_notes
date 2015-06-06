import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)

i=0
while i<10000000:
    i+=1
    GPIO.output(7, True)
    GPIO.output(7, False)
