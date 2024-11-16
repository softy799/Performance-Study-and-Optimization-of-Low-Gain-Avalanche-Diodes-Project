import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Function to define the resistance equation
def resistance_equation(T, A, B, C, D):
    return np.exp(A + B / T + C / T ** 2 + D / T ** 3)

# Read the data from the file
with open("/Users/erronnbridgewater/Downloads/D10.3_data_sheet.txt", "r") as f:
    lines = f.readlines()[1:]


def inverse_resistance_equation (R, a, b, c, d):
    T = np.exp(a + b* np.log(R) + c * np.log(R**2) + d * np.log(R**3))
    return 1/T


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

# Filters data within the temperature range
temp_range_min = 0 + 273.15
temp_range_max = 150 + 273.15

temperature_mask = (np.array(kelvin_list) >= temp_range_min) & (np.array(kelvin_list) <= temp_range_max)
filtered_kelvin_list = np.array(kelvin_list)[temperature_mask]
filtered_ydata = np.array(ydata)[temperature_mask]


# Performs curve fitting to find the optimized values for A, B, C, and D within the temperature range
optimal_values, _ = curve_fit(resistance_equation, filtered_kelvin_list, filtered_ydata, p0=initial_guess)
A_opt, B_opt, C_opt, D_opt = optimal_values


# Prints optimized values for the temperature range
print("Optimized values for temperature range")
print("A:", A_opt)
print("B:", B_opt)
print("C:", C_opt)
print("D:", D_opt)

# Create x_model and y_model for the fitted curve within the temperature range
x_model = np.linspace(temp_range_min, temp_range_max, 150)
y_model = resistance_equation(x_model, A_opt, B_opt, C_opt, D_opt)
y_inverse_model = inverse_resistance_equation(y_model, A_opt, B_opt, C_opt, D_opt)
# Plots the data and the fitted curve
#plt.plot(y_model, x_model, color='r', label="Fitted Curve")
plt.plot(ydata, kelvin_list, label="Data")
#plt.plot(filtered_kelvin_list, filtered_ydata , color='y')
plt.plot (y_inverse_model, x_model, color='g', label="Inverse of Fitted Curve ")
plt.title("Temperature Data and Inverse Equation")
plt.xlabel("Resistance/R25")
plt.ylabel("Temperature (K)")
plt.legend()
plt.tight_layout()
plt.show()