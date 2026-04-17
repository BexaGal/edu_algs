import sympy

x = sympy.symbols('x')
y = x/(x*x + x + 1)
a = (sympy.integrate(y, (x, 2, 7)))
print(a.n(5))
print(sympy.latex(a))
