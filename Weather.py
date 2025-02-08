import adafruit_bme680
import time
import board

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25


for time1 in range(0, 31):
	print("Seconds: ", time1, "Temperature: ",bme680.temperature,"Gas: ", bme680.gas, "Humidity:",bme680.relative_humidity, "Pressure: ", bme680.pressure, "Altitude: ", bme680.altitude)
	time.sleep(1)

