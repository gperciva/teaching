#!/usr/bin/env python

filename = "small.bmp"
file = open(filename, 'rb')
data = file.read(4)
print data
#for d in data[:10]:
#	print d
#	print "%i" % ( int(d) )

