import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def resistance_equation(T, A, B, C, D):
    return np.exp(A + B / T + C / T ** 2 + D / T ** 3)

# Function to calculate the voltage V
def calculate_voltage(V0, R1, R2):
   return V0 * (R2 / (R1 + R2))

# Provide initial guess values for fitting parameters A, B, C, D
initial_guess = [1.0, 1.3, 1.4, 1.5]

with open("/Users/erronnbridgewater/Library/Mobile Documents/com~apple~Numbers/Documents/chamber2.csv", "r") as f:
    lines = f.readlines()[1:]

# Prepare the data
kelvin_list = []
ydata = []
for line in lines:
    parts = line.strip().split(',')
    temperature = float(parts[0])
    resistance = float(parts[1])
    kelvin_list.append(temperature + 273.15)  # Convert to Kelvin
    ydata.append(resistance)  # Populate ydata list

# Filter data within the temperature range (-50 Celsius to 0 Celsius)
temp_range_min = -60 + 273.15
temp_range_max = 180 + 273.15

temperature_mask = (np.array(kelvin_list) >= temp_range_min) & (np.array(kelvin_list) <= temp_range_max)
filtered_kelvin_list = np.array(kelvin_list)[temperature_mask]
filtered_ydata = np.array(ydata)[temperature_mask]

# Performs curve fitting to find the optimized values for A, B, C, and D within the temperature range


#A_opt, B_opt, C_opt, D_opt = optimal_values


#x_model = np.linspace(temp_range_min, temp_range_max, 150)

V0 = 5
R2 = 1  # in ohms


# Calculate the voltage for each data point using the given data
voltages = []
for R1_over_R25 in ydata:
   voltage = calculate_voltage(V0, R1_over_R25, R2)
   voltages.append(voltage)


# Print the calculated voltages
for i, voltage in enumerate(voltages):
   print(f"Calculated voltage for data point {i + 2}: {voltage:.2f} V")



#y_model = resistance_equation(x_model, A_opt, B_opt, C_opt, D_opt)

#plt.plot(x_model, y_model, color='r', label="Fitted Curve")


#plt.plot(filtered_kelvin_list, filtered_ydata, color='y', label="Filtered Data")

print("Optimized values for temperature range (-60 Celsius to 180 Celsius):")
#print("A:", A_opt)

#print("B:", B_opt)

#print("C:", C_opt)


#print("D:", D_opt)

plt.scatter(filtered_kelvin_list, voltages, color='b', label="Voltages for ohms")
plt.legend()
plt.xlabel("Temperature (K)")
plt.ylabel("Voltage (V)")
plt.title("Calculated Voltages vs temperatueres ")
plt.show()

