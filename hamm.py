#!/usr/bin/pypy
import sys

s = [line for line in sys.stdin]
ret = sum (s[0][i] != s[1][i] for i in range(0, len(s[0])))
print ret
