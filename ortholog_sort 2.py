#! /usr/bin/env python
# -*- coding: utf-8 -*-
# *** author: william wang ***

### this script aims to extract orthologous gene cluster names according to match result key_match_orth.py genetated. ###

for i in range(1, 381):
	f1 = open('../key.txt', 'r')
	f2 = open('../pan_single_copy/ortholog%s.fasta'%i, 'r')
	f3 = open('ortholog_sorted%s'%i,'a')

	cluster_keylist = []

	for genes in f2:
		if genes.startswith('>'):
			keyname = genes[1:6]
			cluster_keylist.append(keyname)

	f2 = open('../pan_single_copy/ortholog%s.fasta'%i, 'r')
	keylist = f1.read().split('\t')
	genelist = f2.read().split('>')

	for key in keylist:
		if key in cluster_keylist:
			for gene in genelist:
				if key in gene:
					f3.write('>'+gene)
		else:
			f3.write('>'+key+'\n'+'\n')
		
	f1.close()
	f2.close()
	f3.close()
