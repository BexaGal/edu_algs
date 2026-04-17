import sympy

x = sympy.symbols('x')
y = sympy.cos(x + x**6)
y1 = sympy.diff(y, x)
p = sympy.plotting.plot(y, (x, -10, 10), legend=1, show=False)
p.append(sympy.plotting.plot(y1, (x, -10, 10), legend=1, show=False)[0])
p.show()
