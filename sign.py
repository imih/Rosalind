#!/usr/bin/python
import math, sys
from itertools import permutations

n = 5
print math.factorial(n) * (1 << n)
for perm in permutations([str(i + 1) for i in xrange(n)]):
    for i in xrange(1 << n):
        for j in xrange(n):
            if((i >> j) & 1):
	      sys.stdout.write('-')
            sys.stdout.write(perm[j] + ' ')
	sys.stdout.write('\n')


    


