#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

for i in range(1, 2):
	f1 = open('accumu5_pan_single_copy_nuc.fasta','r')
	f2 = open('accumu5_pan_single_copy_nuc_rename.fasta','w')
	seqs = ''
	for genes in f1:
		genes = genes.strip( )
		if genes.startswith('>'):
			genes = genes.split('_#_')[0]
		
		f2.write(genes+'\n')

	f1.close()
	f2.close()
