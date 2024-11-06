import numpy as np

def integral_trapezoidal(f, a, b, E):
	x = np.linspace(a, b, E+1)
	y = f(x)
	area = (b - a) / E * (np.sum(y) - (y[0] + y[-1]) / 2)
	return area

def f(x):
	return np.sin(x)  

a = 0
b = np.pi

E = 1000

area = integral_trapezoidal(f, a, b, E)
print("Pole powierzchni pod wykresem funkcji:", area)
