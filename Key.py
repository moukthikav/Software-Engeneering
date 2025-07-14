# weather_model_keyboard.py

import numpy as np
import matplotlib.pyplot as plt

# Get number of points and data from user
n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    xi = float(input(f"Enter time x[{i+1}]: "))
    yi = float(input(f"Enter temperature y[{i+1}]: "))
    x.append(xi)
    y.append(yi)

x = np.array(x)
y = np.array(y)

# Fit the quadratic model
coeffs = np.polyfit(x, y, 2)
a, v, c = coeffs

print("Quadratic Equation: y = {:.2f}x² + {:.2f}x + {:.2f}".format(a, v, c))

# Plot the data and the fitted curve
x_curve = np.linspace(min(x), max(x), 100)
y_curve = a * x_curve**2 + v * x_curve + c

plt.scatter(x, y, color='green', label='Input Data')
plt.plot(x_curve, y_curve, color='orange', label='Quadratic Fit')
plt.title("Keyboard Input Weather Data - Quadratic Fit")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
