#!/usr/bin/pypy
import sys
from revc import rev_compl

line = "".join([line.strip() for line in sys.stdin.readlines()[1:]])

for l in xrange(4, min(len(line), 13)):
  for i in xrange(0, len(line) - l + 1):
    if line[i:i+l]== rev_compl(line[i:i+l]):
      print str(i + 1) + " " + str(l)



