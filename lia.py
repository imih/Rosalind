#!/usr/bin/python
from numpy.random import binomial

k, n = 5, 8
print sum(binomial(1 << k, 0.25, 2000000) >= n) / float(2000000)
