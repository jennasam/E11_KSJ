import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inside_data = pd.read_csv("Combo_Data_Inside.csv")
outside_data = pd.read_csv("Combo_Data_Outside.csv")
x0 = inside_data['PM1.0']
x1 = inside_data['PM2.5']
x2 = inside_data['PM10']
x3 = inside_data['Temp']
x4 = inside_data['Gas']
x5 = inside_data['Humidity']
x6 = inside_data['Pressure']
x7 = inside_data['Altitude']

y0 = outside_data['PM1.0']
y1 = outside_data['PM2.5']
y2 = outside_data['PM10']
y3 = outside_data['Temp']
y4 = outside_data['Gas']
y5 = outside_data['Humidity']
y6 = outside_data['Pressure']
y7 = outside_data['Altitude']



plt.hist(x0, label = "inside PM1.0" )
plt.hist(y0, label = "outside PM1.0")
pm1out = outdata.loc[:,'PM1']
pm1in = indata.loc[:,'PM1']
plt.hist(pm1out,label = "outside")
plt.hist(pm1in,label = "inside")
plt.ylabel('time')
plt.xlabel('PM 1.0')
plt.legend()
plt.show()


plt.hist(x1, label = "inside PM2.5")
plt.hist(y1, label = "outside PM2.5")
plt.hist(pm25out,label = "outside")
plt.hist(pm25in,label = "inside")
plt.ylabel('time')
plt.xlabel('PM 2.5')
plt.legend()
plt.show()


plt.hist(x2, label = "inside PM10")
plt.hist(y2, label = "outside PM10")
plt.hist(pm10out,label = "outside")
plt.hist(pm10in,label = "inside")
plt.ylabel('time')
plt.xlabel('PM 10')
plt.legend()
plt.show()


plt.hist(x3, label = "inside temp")
plt.hist(y3, label = "outside temp")
plt.hist(tempout,label = "outside", bins = "auto")
plt.hist(tempin,label = "inside")
plt.ylabel('time')
plt.xlabel('temperature')
plt.legend()
plt.show()


plt.hist(x4, label = "inside Gas")
plt.hist(y4, label = "outside Gas")
plt.hist(gasout,label = "outside", bins = "auto")
plt.hist(gasin,label = "inside")
plt.ylabel('time')
plt.xlabel('Gas')
plt.legend()
plt.show()


plt.hist(x5, label = "inside humidity")
plt.hist(y5, label = "outside humidity")
plt.hist(humidout,label = "outside", bins = "auto")
plt.hist(humidin,label = "inside")
plt.ylabel('time')
plt.xlabel('humidity')
plt.legend()
plt.show()


plt.hist(x6, label = "inside pressure")
plt.hist(y6, label = "outside pressure")
plt.hist(pressureout,label = "outside", bins = "auto")
plt.hist(pressurein,label = "inside")
plt.ylabel('time')
plt.xlabel('pressure')
plt.legend()
plt.show()


plt.hist(x7, label = "inside altitude")
plt.hist(y7, label = "outside altitude")
plt.hist(alout,label = "outside", bins = "auto")
plt.hist(alin,label = "inside")
plt.ylabel('time')
plt.xlabel('altitude')
plt.legend()
plt.show()


std_mean_pm10_in = np.std(x2)/ np.sqrt(300)
print(std_mean_pm10_in)

std_mean_pm10_out = np.std(y2)/ np.sqrt(300)
print(std_mean_pm10_out)

diff = np.abs(std_mean_pm10_in - std_mean_pm10_out)
print(diff)

ans = np.abs(diff/(np.std(x2)/np.sqrt(300)))
print(ans)
