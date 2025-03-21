import RPi.GPIO as GPIO
import datetime
import time
import datetime
 
global count
global cpm
count = 0
x = 0
cpm = 0

def my_callback(channel):
    GPIO.input(channel) == GPIO.HIGH
    global count
    global cpm
    count += 1
    now = datetime.datetime.now()
    print(f'I got an output! The count number is {count}. The time is {now}.') 

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
  
while True:
    time.sleep(1)
    x += 1
    if (x % 60) == 0:
        cpm = count
        print(f'CPM is {cpm}')
