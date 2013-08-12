#!/usr/bin/python

n = 86
m = 16

dp = [1, 1]

while len(dp) < m:
  dp.append(dp[-1] + dp[-2])

while len(dp) < n:
  dp.append(sum (dp[len(dp) - i] for i in xrange(2, m + 1)))

print dp[n - 1]
