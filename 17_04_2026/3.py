import sympy

x = sympy.symbols('x')
y = sympy.symbols('y')
z = x*y + sympy.sin(x)*sympy.cos(y)+x**2
p = sympy.plotting.plot3d(z, (x, -10, 10),(y, -10, 10) , legend=1, show=False)
zx = sympy.diff(z, x)
zy = sympy.diff(z, y)
print(sympy.latex(zx), '\n')
print(sympy.latex(zy), '\n')
p.append(sympy.plotting.plot3d(zx, (x, -10, 10),(y, -10, 10) , legend=1, show=False)[0])
p.append(sympy.plotting.plot3d(zy, (x, -10, 10),(y, -10, 10) , legend=1, show=False)[0])
p.show()
