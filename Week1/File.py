# weather_model_file.py

import numpy as np
import matplotlib.pyplot as plt
import csv

# Read data from CSV file
filename = "C:/Users/MOUKTHIKA/OneDrive/Desktop/data.csv"
x = []
y = []

with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x.append(float(row['time']))
        y.append(float(row['temperature']))

x = np.array(x)
y = np.array(y)

# Fit the quadratic model
coeffs = np.polyfit(x, y, 2)
a, v, c = coeffs

print("Quadratic Equation: y = {:.2f}x² + {:.2f}x + {:.2f}".format(a, v, c))

# Plot the data and the fitted curve
x_curve = np.linspace(min(x), max(x), 100)
y_curve = a * x_curve**2 + v * x_curve + c

plt.scatter(x, y, color='purple', label='File Data')
plt.plot(x_curve, y_curve, color='red', label='Quadratic Fit')
plt.title("File Input Weather Data - Quadratic Fit")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
