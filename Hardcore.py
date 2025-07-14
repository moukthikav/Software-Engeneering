# weather_model_hardcoded.py

import numpy as np
import matplotlib.pyplot as plt

# Hardcoded time (x) and temperature (y) values
x = np.array([1, 2, 3, 4, 5])
y = np.array([30, 32, 35, 33, 31])

# Fit quadratic model: y = ax^2 + vx + c
coeffs = np.polyfit(x, y, 2)
a, v, c = coeffs

print("Quadratic Equation: y = {:.2f}x² + {:.2f}x + {:.2f}".format(a, v, c))

# Plot the data and the fitted curve
x_curve = np.linspace(min(x), max(x), 100)
y_curve = a * x_curve**2 + v * x_curve + c

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_curve, y_curve, color='red', label='Quadratic Fit')
plt.title("Hardcoded Weather Data - Quadratic Fit")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
