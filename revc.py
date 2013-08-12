#!/usr/bin/python

from string import maketrans

rev_compl = lambda org: (org[::-1].translate(maketrans('ACGT', 'TGCA')))
