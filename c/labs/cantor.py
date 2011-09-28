#!/usr/bin/env python

total_width = 81
width = 0  # global var

def cantor(length):
	if (length == 1):
		next = ''
		for i in range(width):
			next += '*'
		return next
	else:
		inside_width = (3**(length-2)) * width
		inside = ''
		for i in range(inside_width):
			inside += ' '
		return cantor(length-1) + inside + cantor(length-1)

for i in range( 1, 6 ):
	width = total_width / (3**(i-1))
	print cantor(i)

