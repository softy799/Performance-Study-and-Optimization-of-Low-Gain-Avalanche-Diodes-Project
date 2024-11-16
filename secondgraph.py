import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame, skipping the first row (header)
data = pd.read_csv('', skiprows=1, header=None)

# Split the DataFrame into x and y data
x = data[0]
y_data = data.iloc[:, 1:]

# Create a figure and axis
fig, ax = plt.subplots()

# Custom labels for each scatter plot
labels = ["NTC (1,500 ohms)", "B", "NTC (10,000 ohms)", "NTC (2,000 ohms)"]

# Plot each y column as scatter points with custom labels for the legend
for i in range(y_data.shape[1]):
    ax.scatter(x, y_data.iloc[:, i], label=labels[i])

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Data Plot')

# Set the y-axis range
ax.set_ylim(-38, 118)

# Add a legend with custom labels
ax.legend()

# Show the plot
plt.show()
