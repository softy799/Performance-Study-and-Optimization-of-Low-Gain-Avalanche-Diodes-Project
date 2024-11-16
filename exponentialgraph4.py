import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Function to define the resistance equation
def resistance_equation(T, A, B, C, D):
    return np.exp(A + B / T + C / T ** 2 + D / T ** 3)

# Read the data from the file
with open("/Users/erronnbridgewater/Downloads/D10.3_data_sheet.txt", "r") as f:
    lines = f.readlines()[1:]


# Prepare the data 

xdata = []
ydata = []
kelvin_list = []

for x in lines:
    a = x.split(',')
    xdata.append(float(a[0]))
    ydata.append(float(a[1]))
    kelvin_list.append(float(a[0]) + 273.15)

# Initial guess for A, B, C, and D
initial_guess = [1.2, 0.5, -0.1, 0.02]

# Filter data within the temperature range (-50 Celsius to 0 Celsius)
temp_range_min = -50 + 273.15
temp_range_max = 150 + 273.15

temperature_mask = (np.array(kelvin_list) >= temp_range_min) & (np.array(kelvin_list) <= temp_range_max)
filtered_kelvin_list = np.array(kelvin_list)[temperature_mask]
filtered_ydata = np.array(ydata)[temperature_mask]

# Performs curve fitting to find the optimized values for A, B, C, and D within the temperature range
optimal_values, _ = curve_fit(resistance_equation, filtered_kelvin_list, filtered_ydata, p0=initial_guess)
A_opt, B_opt, C_opt, D_opt = optimal_values


# Print the optimized values for the temperature range (-50 Celsius to 0 Celsius)
print("Optimized values for temperature range (0 Celsius to 50 Celsius):")
print("A:", A_opt)
print("B:", B_opt)
print("C:", C_opt)
print("D:", D_opt)

# Create x_model and y_model for the fitted curve within the temperature range
x_model = np.linspace(temp_range_min, temp_range_max, 150)
y_model = resistance_equation(x_model, A_opt, B_opt, C_opt, D_opt)

# Plot the data and the fitted curve
plt.plot(x_model, y_model, color='r', label="Fitted Curve")
plt.plot(kelvin_list, ydata, label="Data")
plt.plot(filtered_kelvin_list,
filtered_ydata , color='y', label="Data")
plt.title("Resistance Equation Graph")
plt.xlabel("Temperature (K)")
plt.ylabel("Resistance/R25")
plt.legend()
plt.tight_layout()
plt.show()