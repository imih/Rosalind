#!/usr/bin/pypy

import sys
t = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
ret = []

for i in range(len(t)):
  if t[i:].startswith(s):
    ret.append(str(i + 1))

print " ".join(ret)
