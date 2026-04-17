import sympy

x = sympy.symbols('x')
y = 1/(5*x - 2)
a = (sympy.integrate(y, x))
print(sympy.latex(a))
print(a)
