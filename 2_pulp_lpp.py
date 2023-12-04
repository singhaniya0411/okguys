
!pip install pulp

import pulp
import matplotlib.pyplot as plt

"""This line creates a Linear Programming problem (LP) instance named lp_problem with the objective of maximizing (LpMaximize)."""

lp_problem = pulp.LpProblem("LPP", pulp.LpMaximize)

"""These lines define two decision variables, x and y, with lower bounds set to 0. These variables represent the values you want to find in the optimization."""

x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

"""This line sets the objective function to be maximized. In this case, it's 3x + 2y."""

lp_problem += 3 * x + 2 * y

"""These lines define the constraints of the LP. The first constraint, x <= 4, restricts x to be less than or equal to 4. The second constraint, y <= 6, restricts y to be less than or equal to 6. The third constraint, 2x + y <= 12, restricts the linear combination of x and y to be less than or equal to 12."""

lp_problem += x <= 4
lp_problem += y <= 6
lp_problem += 2 * x + y <= 12

"""This line solves the LP using the PuLP solver. It finds the optimal values for x and y that maximize the objective function within the given constraints."""

lp_problem.solve()

"""This line prints the status of the LP solver, indicating whether it's solved successfully, infeasible, or unbounded."""

print("Status:", pulp.LpStatus[lp_problem.status])

print("x =", x.varValue)
print("y =", y.varValue)

print("Optimal Value =", pulp.value(lp_problem.objective))

x_values = [x.varValue for x in [x, y]]
y_values = [y.varValue for y in [x, y]]



print(x_values, y_values)

"""This line plots a red dot ('ro') at the coordinates determined by the optimal values of x and y, representing the optimal solution."""

plt.plot(x.varValue, y.varValue, 'ro', label="Optimal Value")
plt.fill([0, 4, 4, 3, 0], [0, 0, 4, 6, 6], 'b', alpha=0.2)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Solution of LPP")

plt.legend()

plt.grid(True)
plt.show()

