#!/usr/bin/env python
#msg1 = "Graham is a cat lover."
#msg2 = "DO NOT TRUST HIM!"
msg1 = "cats"
msg2 = "kittens"

def both(text):
	# encryption
	def enc(a, b):
		x = ord(a)
		y = ord(b)
		print x, y
		x = x << 8
		x = x | ord(b)
		print x
		x = x ^ 31337
		return x

	if (len(text) & 1 == 1):
		text += " "

	cypher = []
	for i in range(len(text)>>1):
		number = enc(text[2*i], text[2*i+1])
		cypher.append( number )

	for i in range(len(cypher)):
		print cypher[i],
	print

	# decryption
	def dec(x):
		x = x ^ 31337
		y = x & 255
		x = x >> 8
		return chr(x), chr(y)

	normal = ""
	for i in range(len(cypher)):
		a, b = dec( cypher[i] )
		normal += a + b

	print normal

both(msg1)
both(msg2)

