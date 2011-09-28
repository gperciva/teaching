#!/usr/bin/env python

def cli(text):
	spaces = 0
	periods = 0
	for i in range(len(text)):
		c = text[i]
		if (c == ' '):
			spaces = spaces + 1
		if (c == '.'):
			periods = periods + 1

	words = spaces + 1
	characters = len(text) - periods - spaces
	sentences = periods

	cli = 5.89 * characters/ words - 29.5 * sentences / words - 15.8
	print "total length: ", len(text),
	print "characters: ", characters, "spaces: ", spaces
	print "periods: ", periods, "words ", words
	return cli 



cats = """I like cats. Cats like me. Miao miao miao. Dogs are bad. Bad dogs bad."""

macbeth = """"Tomorrow, and tomorrow, and tomorrow, Creeps in this petty pace from day to day, To the last syllable of recorded time; And all our yesterdays have lighted fools The way to dusty death. Out, out, brief candle. Life's but a walking shadow, a poor player That struts and frets his hour upon the stage And then is heard no more. It is a tale Told by an idiot, full of sound and fury Signifying nothing.  """

abstract = """"Existing computer programs that measure readability are based largely upon subroutines which estimate number of syllables, usually by counting vowels. The shortcoming in estimating syllables is that it necessitates keypunching the prose into the computer.  There is no need to estimate syllables since word length in letters is a better predictor of readability than word length in syllables. Therefore, a new readability formula was computed that has for its predictors letters per hundred words and sentences per hundred words. Both predictors can be counted by an optical scanning device, and thus the formula makes it economically feasible for an organization such as the US Office of Education to calibrate the readability of all textbooks for the public school system.  """

print cli(cats)
print cli(macbeth)
print cli(abstract)


