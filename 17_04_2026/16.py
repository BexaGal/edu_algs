import sympy

x = sympy.symbols('x')
f = (sympy.root(1 + x, 5) - 1)/sympy.sin(x)
print(sympy.limit(f, x, 0))
