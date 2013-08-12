#!/usr/bin/pypy
import math
from itertools import permutations

n = 6
print math.factorial(n)
for perm in permutations([str(i + 1) for i in xrange(n)]):
  print " ".join(perm)

