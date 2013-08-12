#!/usr/bin/pypy
import fasta, bisect

d = fasta.getStrings('grphin')
head = [d[key] for key in sorted(d.keys(), key = d.__getitem__)]

for key in d.keys():
  x = bisect.bisect(head, d[key][-3:])
  while x < len(head) and head[x][0:3] == d[key][-3:]:
    if head[x] != d[key]:
      print key + " " + d.keys()[d.values().index(head[x])]
    x = x + 1



