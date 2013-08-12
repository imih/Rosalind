#!/usr/bin/pypy
import sys
from itertools import product

alf = sys.stdin.readline().strip().split()
n = int(sys.stdin.readline().strip())
for perm in product(alf, repeat=n):
  print "".join(perm)
