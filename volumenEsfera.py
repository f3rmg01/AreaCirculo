from random import random
def volumenEsfera(n):
	cuenta = 0
	for i in range(n):
		x = random()
		y = random()
		z = random()
		if (x**2 + y**2 + z**2) <1:
			cuenta = cuenta + 1
	volumen= cuenta/n
	return volumen

volumenE = volumenEsfera(1000000)
print(8*volumenE)
