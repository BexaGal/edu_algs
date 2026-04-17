import sympy

x = sympy.symbols('x')
f = (sympy.acos(x)**2)/(1-x)
print(sympy.limit(f, x, 1))
