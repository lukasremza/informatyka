def f(x):
	return x**2 - 4

def takie_cos(a, b, tol=1e-6):
	if f(a) * f(b) >= 0:
    	print("Funkcja musi mieć różne znaki na końcach przedziału [a, b]")
    	return None

	while (b - a) / 2 > tol:
    	c = (a + b) / 2
    	if f(c) == 0:
        	return c  
    	elif f(a) * f(c) < 0:
        	b = c
    	else:
        	a = c
	return (a + b) / 2  

root = takie_cos(0, 3)
print("Miejsce zerowe:", root)
