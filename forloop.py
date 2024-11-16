import matplotlib.pyplot as plt 
f = open("/Users/erronnbridgewater/matplotlib_project/stuydingpython/Temperature_data_1-2.txt", "r")
lines = f.readlines()[1:]
xdata = []
ydata = []
y = ydata
x = xdata 
for x in lines:
    a = x.split(',')
    xdata.append(float(a[0]))
    print(xdata)
    ydata.append(float(a[0]))
    print(ydata)

   


     







plt.plot(x,y)
# plt.scatter(x,y)
plt.title("Temperature Data")
plt.xlabel("Duration [mins]")
plt.ylabel("Temperature [C]")

#plt.xlim([0, 101])
#plt.ylim([-39.6, 24.676])

plt.show()
