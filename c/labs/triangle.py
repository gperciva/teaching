#/usr/bin/env python

#from __future__ import print_function
#def printLoop(symbol, iterations):
#	for i in range(iterations):
#		print(symbol, end='')


def triangle(size, array):
	if (size == 1):
		return [['.']]
	add = triangle(size-1, array)
	return next

#	for i in range(size):
#		n = i+1
#		printLoop('*', n)
#		print ()

array = [['.']]
array = triangle(2, array)

#for line in array:	
#	for c in line:
#		print c,

