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


plt.plot(x0)#, label = "time vs PM1.0")
#plt.ylabel('time')
#plt.xlabel('PM 1.0')
#plt.legend()
plt.show()


plt.plot(x1)
plt.show()

plt.plot(x2)
plt.show()

plt.plot(x3)
plt.show()

plt.plot(x4)
plt.show()

plt.plot(x5)
plt.show()

plt.plot(x6)
plt.show()

plt.plot(x7)
plt.show()


plt.plot(x0,y0, label = "PM1.0" )
#plt.ylabel('time')
#plt.xlabel('PM 1.0')
plt.legend()
plt.show()


plt.plot(x1, label = "inside PM2.5")
plt.plot(y1, label = "outside PM2.5")
plt.legend()
plt.show()


plt.plot(x2, label = "inside PM10")
plt.plot(y2, label = "outside PM10")
plt.legend()
plt.show()


plt.plot(x3, label = "inside temp")
plt.plot(y3, label = "outside temp")
plt.legend()
plt.show()


plt.plot(x4, label = "inside Gas")
plt.plot(y4, label = "outside Gas")
plt.legend()
plt.show()


plt.plot(x5, label = "inside humidity")
plt.plot(y5, label = "outside humidity")
plt.legend()
plt.show()


plt.plot(x6, label = "inside pressure")
plt.plot(y6, label = "outside pressure")
plt.legend()
plt.show()


plt.plot(x2, label = "inside altitude")
plt.plot(y2, label = "outside altitude")
plt.legend()
plt.show()
