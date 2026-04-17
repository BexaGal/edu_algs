import sympy

x = sympy.symbols('x')
y = x/sympy.sqrt(1 + x**4)
a = (sympy.integrate(y, x))
print(sympy.latex(a))
print(a)
