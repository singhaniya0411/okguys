
from sympy import symbols, diff, solve, Matrix

# Define the variables
x, y, l = symbols('x y lambda')

# Define the objective function and constraint
f = x**2 + y**2
g = x + y - 1

# Define the Lagrangian
L = f - l * g

# Compute partial derivatives
partials = [diff(L, var) for var in (x, y, l)]

# Solve the system of equations
solution = solve(partials, (x, y, l), dict=True)[0]

# Extract the optimal values
optimal_x = solution[x]
optimal_y = solution[y]

# Compute the Hessian matrix
# hessian_matrix = Matrix([[diff(L.diff(var1), var2) for var1 in (x, y, l)] for var2 in (x, y, l)])

# Compute the Hessian matrix using a list of lists
hessian_list = []

# Iterate over var2
for var2 in (x, y, l):
    # Initialize a row for var2
    row = []

    # Iterate over var1
    for var1 in (x, y, l):
        # Calculate the second-order partial derivative and append to the row
        row.append(diff(L.diff(var1), var2))

    # Append the row to the Hessian list
    hessian_list.append(row)

# Create an instance of the Matrix class from the list of lists
hessian_matrix = Matrix(hessian_list)

# Display the Hessian matrix
print(hessian_matrix)




# Check the definiteness of the Hessian at the stationary point
hessian_determinant = hessian_matrix.det()
if hessian_determinant > 0:
    print("Stationary point is a local minimum.")
elif hessian_determinant < 0:
    print("Stationary point is a local maximum.")
else:6
    print("Second-order test inconclusive (saddle point or test fails).")

# Display the result
print("Optimal solution:")
print(f"x: {optimal_x}")
print(f"y: {optimal_y}")
