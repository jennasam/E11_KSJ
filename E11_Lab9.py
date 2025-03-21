import RPi.GPIO as GPIO
import datetime
import time
import datetime
 
global count
count = 0

def my_callback(channel):
    GPIO.input(channel) == GPIO.HIGH
    global count
    count += 1
    now = datetime.datetime.now()
    print(f'I got an output! The count number is {count}. The time is {now}') 

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
  
while True:
    time.sleep(10)

