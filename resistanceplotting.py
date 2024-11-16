import matplotlib.pyplot as plt 

temperatures = [23.6, 0, -10, -20, -30, -40, -50, -60]

resistances = [1.042, 3.391, 5.765, 10.16, 1.054, 35.87, 72.5, 148.9]

plt.plot(temperatures, resistances, marker='o', linestyle='-', color='b')

plt.xlabel ('Temperature')

plt.ylabel ('Resistance (Kilohms)')

plt.title ('Resistance vs. Temperature')

plt.grid (True)

plt.show()