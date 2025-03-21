import RPi.GPIO as GPIO
import datetime
import time
 
def my_callback(channel):
    GPIO.input(channel) == GPIO.HIGH
    print('I got an output!')
 

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
  
while True:
    time.sleep(10)

