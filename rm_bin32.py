#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***


f1 = open('accumu6_nuc_add_cluster.fasta','r')
f2 = open('accumu5_nuc_add_cluster.fasta', 'w')

seqlist = f1.read().split('>')

for gene in seqlist:
	if 'Bin32.1' not in gene:
		f2.write('>'+gene)

f1.close()
f2.close()