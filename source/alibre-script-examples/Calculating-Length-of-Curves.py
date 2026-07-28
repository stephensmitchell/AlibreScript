#https://help.alibre.com/articles/#!alibre-help-v23/calculating-length-of-curves
import sympy
from sympy import *
x = Symbol('x')
formula = 2 * x**2
x_minimum = 5.0
x_maximum = 10.0
d = diff(formula, x)
i = integrate(sqrt(1 + d**2), (x, x_minimum, x_maximum))
length = i.evalf()
print 'Length of curve over x=%.3f to x=%.3f is %.3f mm' % (x_minimum, x_maximum, length)