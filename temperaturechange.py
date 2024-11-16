import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the voltage V
def calculate_voltage(V0, R1, R2):
    return V0 * (R2 / (R1 + R2))

# Read the data from the file
with open("/Users/erronnbridgewater/Downloads/D10.3_data_sheet.txt", "r") as f:
    lines = f.readlines()[1:]

# Prepare the data
xdata = []
ydata_fraction = []
for line in lines:
    a = line.strip().split(',')
    xdata.append(float(a[0]))
    ydata_fraction.append(float(a[1]))

V0 = 5
R2_values = [1.5, 10, 2]  #in kilohms, multiply the value by 1000

voltages_R2_15 = []
voltages_R2_10 = []
voltages_R2_02 = []

# Calculates the voltages for each R2 value 
for R1_over_R25 in ydata_fraction:
    for R2 in R2_values:
        voltage = calculate_voltage(V0, R1_over_R25, R2)
        if R2 == 1.5:
            voltages_R2_15.append(voltage)
        elif R2 == 10:
            voltages_R2_10.append(voltage)
        elif R2 == 2:
            voltages_R2_02.append(voltage)


#print(f"Calculated voltage for data point {i + 2}: {voltage:.2f} V")
plt.plot(xdata, voltages_R2_15, label="R$_{fx}$ = 1.5 kΩ")
plt.plot(xdata, voltages_R2_10, label="R$_{fx}$ = 10 kΩ")
plt.plot(xdata, voltages_R2_02, label="R$_{fx}$ = 2 kΩ")
plt.legend ()
#plt.plot(xdata, voltages)
#plt.plot(filtered_kelvin_list, filtered_ydata , color='y')
plt.title("Voltage Readout for Corresponding Temperatures and Different Resistance")
plt.xlabel("Temperature")
plt.ylabel("Voltage")
plt.show()