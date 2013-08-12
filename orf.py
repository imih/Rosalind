#!/usr/bin/pypy
import sys, fasta, prot, revc

dna = fasta.getStrings('orfin').values()[0]
dna2 = revc.rev_compl(dna)
dna.replace('T', 'U')
dna2.replace('T', 'U')
S = set()

for i in xrange(0, len(dna) - 3):
  s = prot.dna_prot(dna[i:])
  s2 = prot.dna_prot(dna2[i:])
  if s.startswith('M'):
    S.add(s)
  if s2.startswith('M'):
    S.add(s2)

print "\n".join(S)

