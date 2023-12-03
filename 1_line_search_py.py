
import numpy as np

# Define the objective function you want to optimize
def objective_function(x):
    return x**2 + 2*x + 1  # Example: f(x) = x^2 + 2x + 1

# Define the derivative of the objective function
def derivative(x):
    return 2*x + 2  # Example: f'(x) = 2x + 2

# Line Search method for optimization
def line_search_optimization(learning_rate, initial_x, num_iterations):
    x = initial_x
    for i in range(num_iterations):
        gradient = derivative(x)
        x = x - learning_rate * gradient
    return x

# Initial guess and hyperparameters
initial_guess = 0.0
learning_rate = 0.1
num_iterations = 100

# Perform Line Search optimization
optimal_solution = line_search_optimization(learning_rate, initial_guess, num_iterations)

# Print the result
print("Optimal Solution:", optimal_solution)
print("Objective Value at Optimal Solution:", objective_function(optimal_solution))

