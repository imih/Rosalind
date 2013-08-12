#!/usr/bin/pypy
import fasta

d = fasta.getStrings('lcsmin')
s = sorted(d.values())

ok = 0
for l in xrange(len(s[0]), 1, -1):
  if ok == 0 :
    for i in range(0, len(s[0]) - l + 1):
      if all(s[0][i : i + l] in s[j] for j in range(0, len(s))):
	print s[0][i : i + l]
	ok = 1
	break
