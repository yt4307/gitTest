y = lambda x: (1+x)**(1/x)

def lim0(f):
	h = 1e-7
	derv = f(h)
	return derv

print(lim0(y))