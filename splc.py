#!/usr/bin/pypy
import fasta, prot

d = fasta.getStrings('splcin')
f = open('splcin', 'r')
dna = d[f.readline()[1:-1]]
for intron in d.values():
  if intron != dna:
    dna = dna.replace(intron, '')
dna = dna.replace('T', 'U')
print prot.dna_prot(dna)
