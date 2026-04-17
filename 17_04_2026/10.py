import sympy

x = sympy.symbols('x')
f = (1+1/x)**x
print(sympy.limit(f, x, sympy.oo).n(5))
