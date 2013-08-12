#!/usr/bin/pypy
import sys, fasta

ret = ""
dnas = fasta.getStrings('longin').values()

def superstring(dnas, ss = ''):
  if len(dnas) == 0:
    return ss
  
  if len(ss) == 0:
    ss = dnas[0]
    dnas.remove(dnas[0])
    return superstring(dnas, ss)
  for dna in dnas:
    for j in range(len(dna) / 2):
      if ss.startswith(dna[j:]):
	dnas.remove(dna)
	return superstring(dnas, dna[:j] + ss)
      if ss.endswith(dna[:len(dna) - j]):
	dnas.remove(dna)
	return superstring(dnas, ss + dna[len(dna) -j :])

print superstring(dnas)
