import RPi.GPIO as GPIO
import datetime
import time
import datetime

global count
global cpm
count = 0
x = 0
cpm = 0

file = open("Unshielded.csv", "w", newline = None)
file_writer = csv.writer(file)
file_writer.writerow(("CPM", "Time"))

def my_callback(channel):
    global count
    count += 1
    now = datetime.datetime.now()
    print(f'I got an output! The count number is {count}. The time is {now}.') 

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
  
while True:
    time.sleep(60)
    cpm = count
    count = 0
    print(f'CPM is {cpm}')


file_writer.writerow(count, now)

file.close()
