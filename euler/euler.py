a, b = 3, 5
s = 0

for i in xrange(1, 1000):
	if (a * i) < 1000: 
		s += (a *i)
	if (b * i) < 1000 and (b * i) % a != 0:
		s += (b * i)

print s
