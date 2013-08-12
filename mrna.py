#!/usr/bin/pypy
import sys

f = open('codon_comb', 'r')
d = dict()

for line in f.readlines():
  args = line.split()
  d[args[0]] = int(args[1])

prot = sys.stdin.readline()
prot = prot[:-1]
ret = d['Stop']
for i in range(len(prot)):
  ret = (ret * d[prot[i]]) % 1000000
print ret
