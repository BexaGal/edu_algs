import sympy

x = sympy.symbols('x')
f = (sympy.E**x - sympy.E**(-x))/sympy.log(1 + x, sympy.E)
print(sympy.limit(f, x, 0))
print(sympy.limit(f, x, 0).n(5))
