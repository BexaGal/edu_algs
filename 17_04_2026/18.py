import sympy

x = sympy.symbols('x')
f = sympy.log(1 + 3*x, sympy.E)/sympy.tan(2*x)
print(sympy.limit(f, x, 0))
print(sympy.limit(f, x, 0).n(5))
