import matplotlib.pyplot as plt
with open("/Users/erronnbridgewater/matplotlib_project/stuydingpython/Temperature_data_1-2.txt", "r") as f:
    lines = f.readlines()[1:] 

xdata = []
ydata = []
ROWS = (xdata, ydata)
for x in lines:
    a = x.split(',')
    xdata.append(float(a[0]))
    ydata.append(float(a[1]))


# Plots the data
plt.plot(xdata, ydata)
plt.title("Temperature Data")
plt.xlabel("Duration [mins]")
plt.ylabel("Temperature [C]")


# sets x-axis and y-axis limits
# plt.xlim(0, 101)
# plt.ylim(-39.6, 30)
plt.show()