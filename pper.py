#!/usr/bin/pypy

n, k = 81, 10
ret = 1
for i in xrange(n - k + 1, n + 1):
  ret = (ret * i) % 1000000

print ret
