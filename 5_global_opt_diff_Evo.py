import numpy as np
from scipy.optimize import differential_evolution

# Define the function to minimize
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Define bounds for the optimization
bounds = [(-10, 10)]  # Adjust bounds as needed

# Use differential evolution to find the global minimum
result = differential_evolution(objective_function, bounds)

# Extract the optimal solution
global_min_x = result.x
global_min_f = result.fun

print("global min x: ",global_min_x)
print("Global Optimal Solution:")
print(f"x = {global_min_x[0]}")
print(f"f(x) = {global_min_f}")