a, b = 3, 5
res = 0

for i in xrange(1, 1000):
	if (a * i) < 1000: 
		res += (a *i)
	if (b * i) < 1000 and (b * i) % a != 0:
		res += (b * i)

print res
