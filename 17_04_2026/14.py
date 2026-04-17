import sympy

x = sympy.symbols('x')
y = x/sympy.sqrt(3 + 2*(x**2))
a = (sympy.integrate(y, x))
print(sympy.latex(a))
print(a)
