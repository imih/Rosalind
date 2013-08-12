#!/usr/bin/python

import sys

n =33 
k =3

dp=[]
dp.append(1)
dp.append(1)
while len(dp) < n:
  dp.append(dp[-1] + k * dp[-2])

print dp[n-1]
