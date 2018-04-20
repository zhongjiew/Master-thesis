#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

for i in range(1, 381):
	f1 = open('../4.1.mafft/mafft_coregene%s.fasta'%i,'r')
	f2 = open('renamed_ortholog_sorted%s'%i,'w')
	#genelist = f1.read().split('>')
	seqs = ''
	for genes in f1:
		genes = genes.strip( )
		if genes.startswith('>'):
			genes = genes[:6]
		
		f2.write(genes+'\n')

	f1.close()
	f2.close()