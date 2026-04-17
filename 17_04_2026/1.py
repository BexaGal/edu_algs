#import matplotlib
import sympy

x = sympy.symbols('x')
y = x*sympy.log(2, x) + sympy.sin(x)**2
print(sympy.latex(y), '\n')
y1 = sympy.diff(y,x,1)
print(sympy.latex(y1), '\n')
y2 = sympy.diff(y,x,2)
print(sympy.latex(y2), '\n')
y4 = sympy.diff(y,x,4)
print(sympy.latex(y4), '\n')
p = sympy.plotting.plot(y, (x, -10, 10), legend=1, color='b', show=False)
p.append(sympy.plotting.plot(y1, (x, -10, 10), legend=1, color='b', show=False)[0])
p.append(sympy.plotting.plot(y2, (x, -10, 10), legend=1, color='b', show=False)[0])
p.append(sympy.plotting.plot(y4, (x, -10, 10), legend=1, color='b', show=False)[0])
p.show()
