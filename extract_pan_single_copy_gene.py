#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang***

### this script aims to extract orthologous gene cluster names according to match result key_match_orth.py genetated. ###

f1 = open('key.txt', 'r')
f2 = open('out.rhodo.mci.I11', 'r')
f3 = open('clade10_orf_pro.fasta', 'r')
f4 = open(r'pan_single_copy.I11.txt','w')
f5 = open('clade10_orf_pro_pan_single_copy.fasta', 'w')

keylist = f1.read().split('\t')
orth = f2.readlines()
seqs = f3.read().split('>')
psclist = []

for eachline in orth:
		b = 0
		arr = eachline.strip('\n')
		for key in keylist:
			a = arr.count(key)
			b += a
			if a > 1:
				b = 0; break
		if b >= 7:
			f4.write(eachline)
			genes = eachline.split('\t')
			for gene in genes:
				psclist.append(gene.strip())
for seq in seqs:
	name = seq.split('\n')[0]
	if name in psclist:
		f5.write('>'+seq)

	
f1.close()
f2.close()
f3.close()
f4.close()