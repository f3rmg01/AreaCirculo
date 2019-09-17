import random

def areaElipse(n):
	cuenta=0
	for i in range(n):
		x = random.uniform(0,2)
		y = random.uniform(0,1)
		if (x**2)/4 + (y**2)<1:
			cuenta = cuenta + 1
	areaN = 2*cuenta/n
	return areaN

area = areaElipse(10000)
print(4*area)
