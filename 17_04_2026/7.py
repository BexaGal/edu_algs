import sympy

x = sympy.symbols('x')
y = sympy.exp((-x**2)/2)
a = sympy.integrate(y, (x, -sympy.oo, sympy.oo))
print(a)
print(sympy.latex(a))
