#!/usr/bin/pypy
import sys

f =  open('protein_mass', 'r')
d = dict()
for line in f:
  args = line.split()
  d[args[0]] = float(args[1])
f.close()
protein = sys.stdin.readline()[:-1]
print sum(d[protein[i]] for i in xrange(len(protein)))
