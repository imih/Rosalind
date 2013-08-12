#!/usr/bin/python

k, m, n= 19, 15, 23

ret = (m * m - m) / 4.0 + m * n + n * n - n
ret /= (k + m + n) * (k + m + n - 1)
print 1 - ret
