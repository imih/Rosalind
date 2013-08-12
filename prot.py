#!/usr/bin/pypy

import sys

def dna_prot(dna):
	dna = dna.replace('T', 'U')
	f = open('rna_codon')
	args = []
	for line in f:
  		args += line.split()
	f.close()
	d = dict(zip(args[0::2], args[1::2]))

	ret = ""
	for i in xrange(0, len(dna) - 2, 3):
  		if d[dna[i: i + 3]] == 'Stop':
    			return ret
  		ret += d[dna[i:i + 3]]

	return ""
