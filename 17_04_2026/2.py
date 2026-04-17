import sympy

x = sympy.symbols('x')
a= sympy.symbols('a')
y = x**sympy.sin(x) + sympy.sin(x)**a + a**2
yx = sympy.diff(y, x)
ya = sympy.diff(y, a)
print(sympy.latex(yx), '\n')
print(sympy.latex(ya), '\n')
