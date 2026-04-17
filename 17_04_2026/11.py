import sympy

x = sympy.symbols('x')
f = sympy.atan(1/(1-x))
a = sympy.limit(f, x, 1, '-')
b = sympy.limit(f, x, 1, '+')
print(a, b)
