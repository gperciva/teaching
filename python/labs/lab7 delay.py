# -*- coding: utf-8 -*-
class Delay:
   def __init__(self, n):
     self.state = [0]*n
     self.n = n
   def delay(self, inp):
     result = self.state + inp[:-self.n]
     self.state = inp[self.n + 1:]
     return result
   def process(self, inp):
     self.state = [inp] + self.state[:-1]
     return self.state
