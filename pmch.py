#!/usr/bin/pypy
from math import factorial
import sys

s = "".join(sys.stdin.readlines()[1:])
print s
print factorial(s.count('A')) * factorial(s.count('G'))
