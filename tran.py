#!/usr/bin/python
import sys

lines = sys.stdin.readlines()
s = ""
cur = ""
for line in lines[1:]:
  if line.startswith('>'):
    s = cur
    cur = ""
  else:
    cur += line.strip()

t = cur
trans, tranv = 0, 0

for (x, y) in zip(s, t):
  if x == y:
    continue
  if x + y in ["AG", "GA", "CT", "TC"]:
    trans = trans + 1
  if x + y in ["AC", "CA", "AT", "TA", "GC", "CG", "TG", "GT"]:
    tranv = tranv + 1

print float(trans) / float(tranv)


