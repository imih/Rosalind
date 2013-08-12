#!/usr/bin/python
import sys, urllib2, re

proteins = sys.stdin.read().strip().split('\n')
for prot in proteins:
  f = urllib2.urlopen('http://www.uniprot.org/uniprot/' + prot + '.fasta')
  cur = ''.join(f.read().split('\n')[1:])
  ind = []
  for m in re.finditer('(?=(N[^P][ST][^P]))', cur):
    ind.append(m.start() + 1)
  if ind != []:
    print prot
    print ' '.join(map(str, ind))
