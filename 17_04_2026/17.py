import sympy

x = sympy.symbols('x')
f = (3**x - x**3)/(x - 3)
print(sympy.limit(f, x, 3))
print(sympy.limit(f, x, 3).n(5))
