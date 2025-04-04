import RPi.GPIO as GPIO
import datetime
import time
import datetime
import csv

global count
global count_per_10_seconds
count = 0
x = 0
count_per_10_seconds = 0

file = open("Unshielded.csv", "w", newline = None)
file_writer = csv.writer(file)
file_writer.writerow(["count_per_10_seconds", "time"])

def my_callback(channel):
    global count
    count += 1
    now = datetime.datetime.now()
    print(f'I got an output! The count number is {count}. The time is {now}.') 

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)

start_time = time.time()
end_time = start_time + 5

try:
    while time.time() < end_time:
        time.sleep(10)
        count_per_10_seconds = count
        count = 0
        now = datetime.datetime.now()
        print(f'Counts every ten seconds is {count_per_10_seconds}')
        file_writer.writerow([count_per_10_seconds, now])

except KeyboardInterrupt:
    print("Program terminated by user.")

        
file.close()
