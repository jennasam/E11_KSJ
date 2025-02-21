import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
import adafruit_bme680
import sys


reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data...")

import csv
import numpy as np
import time
from datetime import datetime
file = open("PM_Ada.csv", "w", newline = None)
file_writer = csv.writer(file)
file_writer.writerow(("Time", "PM1.0", "PM2.5", "PM10", "Temp", "Gas", "Humidity", "Pressure", "Altitude"))

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25

run_time = 31
if len(sys.argv) < 2:
  print("Script requires run_time(int) as an input")
  exit()
else:
  run_time = int(sys.argv[1])


def combodata(time1):
    i = 0
    while i <= time1:
        time.sleep(1)
        #print("Seconds: ", time1, "Temperature: ",bme680.temperature,"Gas: ", bme680.gas, "Humidity:",bme680.relative_humidity, "Pressure: ", bme680.pressure, "Altitude: ", bme680.altitude)

        try:
            aqdata = pm25.read()
        except RuntimeError:
            print("Unable to read from sensor, retrying...")
            continue

        file_writer.writerow([datetime.fromtimestamp(time.time()), aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude])
        i += 1


        print()
        print("Concentration Units (standard)")
        print("---------------------------------------")
        print(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
        )
        print("Concentration Units (environmental)")
        print("---------------------------------------")
        print(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
        )
        print("---------------------------------------")
        print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
        print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
        print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
        print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
        print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
        print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
        print("---------------------------------------")

        file.close()

    return
    
combodata(run_time)
