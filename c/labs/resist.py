def ohm(volts, resist):
	return resist / volts

def series(r1, r2):
	return r1+r2

def parallel(r1, r2):
	return 1.0 / (1.0/r1 + 1.0/r2)

def par3(r1, r2, r3):
	return 1.0 / (1.0/r1 + 1.0/r2 + 1.0/r3)


r1=100
r2=200
r3=300
r4=400
r5=500
r6=600
r7=700

R = par3( series(r1, r2),
	parallel(r3, r4),
	series(r5, parallel(r6, r7)))
print "the 100 ones:", R, "ohms"
print "overall current:", 12.0 / R * 1000.0, "mA"


r1=123
r2=234
r3=345
r4=456
r5=567
r6=678
r7=789
R = par3( series(r1, r2),
	parallel(r3, r4),
	series(r5, parallel(r6, r7)))
print "the 123 ones:", R, "ohms"
print "overall current:", 12.0 / R * 1000.0, "mA"

