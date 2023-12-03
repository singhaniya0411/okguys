
import math

print(math.sqrt(9))

import sympy

sympy.sqrt(3)

sympy.sqrt(8)

from sympy import symbols

x, y = symbols('x y')



expr = x + 2*y

expr

expr + 1

expr - x

x*expr

from sympy import expand, factor

expanded_expr = expand(x*expr)

expanded_expr

factor(expanded_expr)

from sympy import *

x, t, z, nu = symbols('x t z nu')

init_printing(use_unicode=True)

d_ = diff(sin(x)*exp(x), x)

d_.subs(x, 10)

integrate(exp(x)*sin(x) + exp(x)*cos(x), x)

integrate(sin(x**2), (x, -oo, oo))

solve(x**2 - 2, x)

"""WAP to compute the gradient and Hessian of the function
𝑓(𝑥) = 100(𝑥2 − 𝑥1^2)^2 + (1 − 𝑥1)^2
"""

import sympy as sp

# Define the variables and the function
x1, x2 = sp.symbols('x1 x2')
f = 100 * (x2 - x1**2)**2 + (1 - x1)**2

x1

x2

f

# Compute the gradient (first-order partial derivatives)
grad_f = [sp.diff(f, x1), sp.diff(f, x2)]

# Compute the Hessian (second-order partial derivatives)
hessian_f = [[sp.diff(grad_f[0], x1), sp.diff(grad_f[0], x2)],
             [sp.diff(grad_f[1], x1), sp.diff(grad_f[1], x2)]]

# Display the results
print("Gradient (df/dx1, df/dx2):", grad_f)
print("Hessian Matrix:")
for row in hessian_f:
    print(row)

