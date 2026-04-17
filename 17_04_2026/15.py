import sympy

x = sympy.symbols('x')
y = sympy.log(1 + x**2, sympy.E)
a = (sympy.integrate(y, x))
print(sympy.latex(a))
print(a)
