
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Generate x values
x = np.linspace(-10, 10, 1000)

# Calculate corresponding y values
y = f(x)

np.min(y)

# Find the index of the minimum value
min_index = np.argmin(y)

# Find the global minimum
global_min_x = x[min_index]
global_min_y = y[min_index]

# Plot the function
plt.plot(x, y, label='f(x)')
plt.scatter(global_min_x, global_min_y, color='red', marker='o', label='Global Minimum')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Global Optimization of f(x)')
plt.grid(True)
plt.show()

# Display the global minimum
print(f"Global Minimum: f({global_min_x}) = {global_min_y}")

