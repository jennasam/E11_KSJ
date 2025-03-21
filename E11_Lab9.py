import RPi.GPIO as GPIO
import datetime
import time
import datetime
 
global count
count = 0
x = 0

def my_callback(channel):
    time.sleep(1)
    GPIO.input(channel) == GPIO.HIGH
    global count
    count += 1
    now = datetime.datetime.now()
    x += 1
    if (x % 60) = 0:
        cpm = count
    print(f'I got an output! The count number is {count}. The time is {now}. CPM is {cpm}') 

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
  
while True:
    time.sleep(10)

