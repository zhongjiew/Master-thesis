#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

f1 = open('accumu6_orf_pro_good.fasta','r')
f2 = open('../2.0.prodigal/accumu6_orf_nuc.fasta','r')
f3 = open('accumu6_orf_nuc_good.fasta', 'w')

gene_pros = f1.read().split('>')
gene_nucs = f2.read().split('>')

for gene_pro in gene_pros:
	pro_name = gene_pro.split('\n')[0]
	for gene_nuc in gene_nucs:
		nuc_name = gene_nuc.split('\n')[0]
		if nuc_name == pro_name:
			f3.write(">"+gene_nuc)
			break

f1.close()
f2.close()
f3.close()
