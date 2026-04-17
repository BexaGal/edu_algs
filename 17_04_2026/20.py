import sympy

x = sympy.symbols('x')
f = (sympy.E**(5*x) - sympy.E**(3*x))/sympy.sin(x)
print(sympy.limit(f, x, 0))
print(sympy.limit(f, x, 0).n(5))
