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

j = 0;
for i in range(len(s)):
  if j < len(t) and t[j] == s[i]:
    sys.stdout.write(str(i + 1) + ' ')
    j = j + 1
sys.stdout.write('\n')
