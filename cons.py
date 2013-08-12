#!/usr/bin/pypy
import sys

d = dict(zip([0, 1, 2, 3], ['A', 'C', 'G', 'T']))
stat = [[0 for i in range(4)] for i in range(2000)]
strings = []
cur = ""

for line in sys.stdin:
  if line.startswith('>'):
    if len(cur) > 0:
      strings.append(cur)
      cur = ""
  else:
    cur += line.strip()
strings.append(cur)

n = len(strings[0])
s = "".join(strings)
for i in range(n):
  stat[i][0] = s[i::n].count('A')
  stat[i][1] = s[i::n].count('C')
  stat[i][2] = s[i::n].count('G')
  stat[i][3] = s[i::n].count('T')

s = ""
for i in range(n):
  s += d[stat[i].index(max(stat[i]))]

print s
print "A: " + " ".join(str(stat[i][0]) for i in range(n))
print "C: " + " ".join(str(stat[i][1]) for i in range(n))
print "G: " + " ".join(str(stat[i][2]) for i in range(n))
print "T: " + " ".join(str(stat[i][3]) for i in range(n))
