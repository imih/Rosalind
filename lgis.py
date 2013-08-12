#!/usr/bin/python
import sys, bisect

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().strip().split()]

def lis(X):
  M = [None] * len(X)
  P = [None] * len(X)

  L = 1
  M[0] = 0
    
  for i in range(1, n):
    lo = 0
    hi = L
    
    while lo < hi:
      mid = (lo + hi + 1) // 2
      if X[M[mid - 1]] < X[i]:
	lo = mid
      else :
	hi = mid - 1
    j = lo

    P[i] = M[j - 1]

    if j == L or X[i] < X[M[j]]:
      M[j] = i
      L = max(L, j + 1)

  ret = []
  pos = M[L -1]
  for _ in range(L):
    ret.append(X[pos])
    pos = P[pos]
  return ret[::-1]
 
print ' '.join(map(str, lis(a)))
print ' '.join(map(str, lis(a[::-1])[::-1]))

