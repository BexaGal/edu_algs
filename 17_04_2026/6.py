import sympy

x = sympy.symbols('x')
y = sympy.exp((-x**2)/2)
a = sympy.integrate(y)
print(sympy.latex(a))
