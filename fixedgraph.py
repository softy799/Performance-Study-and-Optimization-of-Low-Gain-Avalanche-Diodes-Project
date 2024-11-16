import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Function to calculate the voltage V
# R1: fixed resistance
# R2: NTC resistance
# V0: fixed voltage of the voltage divider

def inverse_resistance_equation (R, a, b, c, d):
   T = np.exp(a + b* np.log(R) + c * np.log(R**2) + d * np.log(R**3))
   return 1/T


def calculate_voltage(V0, R1, R2):
    return V0 * (R2 / (R1 + R2))

def resistance_equation(T, A, B, C, D):
    return np.exp(A + B / T + C / T ** 2 + D / T ** 3)

# Provide initial guess values for fitting parameters A, B, C, D
initial_guess = [1.0, 1.3, 1.4, 1.5]
f = open("/Users/erronnbridgewater/Library/Mobile Documents/com~apple~Numbers/Documents/chamber2.csv", "r")
lines = f.readlines()[1:]

# Prepare the data
kelvin_list = []
ydata = []
for line in lines:
    parts = line.strip().split(',')
    temperature = float(parts[0])
    resistance = float(parts[1])
    kelvin_list.append(temperature + 273.15)  # Convert to Kelvin
    ydata.append(resistance/1000)  # Populate ydata list: converting to Kohms

# Filter data within the temperature range (-50 Celsius to 180 Celsius)
temp_range_min = -60 + 273.15
temp_range_max = 180 + 273.15

# temperature_mask = (np.array(kelvin_list) >= temp_range_min) & (np.array(kelvin_list) <= temp_range_max)
# filtered_kelvin_list = np.array(kelvin_list)[temperature_mask]
# filtered_ydata = np.array(ydata)[temperature_mask]

# Performs curve fitting to find the optimized values for A, B, C, and D within the temperature range
optimal_values, _ = curve_fit(resistance_equation, kelvin_list, ydata, p0=initial_guess)
A_opt, B_opt, C_opt, D_opt = optimal_values

x_model = np.linspace(temp_range_min, temp_range_max, 150)
y_model = resistance_equation(x_model, A_opt, B_opt, C_opt, D_opt)
y_inverse_model = inverse_resistance_equation(y_model, A_opt, B_opt, C_opt, D_opt)

plt.plot(x_model, y_model, color='r', label="Fitted Function R$_{NTC}$ = exp(A + B / T + C / T$^2$ + D / T$^3$)")

plt.scatter(kelvin_list, ydata, color='black', label="Data")
plt.plot (x_model, y_inverse_model, color='g', label="1/T = a + b * ln(R) + c * ln(R$^2$) + d * ln(R$^3$)")


print("Optimized values for temperature range (-60 Celsius to 180 Celsius):")
print("A:", A_opt)
print("B:", B_opt)
print("C:", C_opt)
print("D:", D_opt)

plt.legend()
plt.ylabel("Temperature (K)")
plt.xlabel("Resistance (K$\Omega$)")
plt.title("Resistance vs Temperature of the NTC Thermistor")
plt.show()