#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

# select gene sequence of coregene or species-specific gene.

import re

f1 = open('pan_single_copy.I11', 'r')
f2 = open('11accumu.orf.pro.fasta', 'r')
f3 = open('coregene_seq_nuc.fasta', 'w')
f4 = open('coregene_name_list', 'w')

#seqs = f2.readlines()

accumulist = []

for line in f1:
	s = re.search('(UW-1.*)', line)
	if s:
		uw = s.group(1).split('\t')[0]
		accumulist.append(uw)
	else:
		accumulist.append(line.split()[0])
seqs = f2.read()
seq_list = seqs.split('>')
for seq in seq_list:
	for a in accumulist:
		if a in seq:
			f3.write('>'+seq)
for a in accumulist:
	f4.write(a+'\n')
	
f1.close()
f2.close()
f3.close()
f4.close()
